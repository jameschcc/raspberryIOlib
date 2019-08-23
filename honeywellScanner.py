import threading
import time

fp = open("/dev/hidraw0", "rb")
#hidrawXX: the number can be found through inputing "ls /dev" in linux console.
#hidrawXX: 在控制台界面输入ls /dev可以看到对应的编号

signs = {40:'EOL',45:'-',46:'-',54:',',55:'.',56:':',51:"'",48:'|',47:'}',49:'{'}
def codeTranslate(code):
  # Number 数字
  if code[0]== 0 and code[2]!=0:
    if code[2]<40:
      return str((code[2]+1)%10)
    if code[2]==40:
        return 'EOL'
    global signs
    # Signs 数字符号
    return signs[code[2]] if (code[2] in signs) else "x%d"%(code[2])
  if code[0]==2:
    # Alphabets [0#:2, 2#:N] 字母
    if code[2]<30 and code[2]>=4:
     return chr(int(code[2])-4+65)
     # Breaks 间歇符号
    else:
      # if code[8]==2:
        return ''
      # else:
        # return "y%d"%(code[2])
  return ''
  pass


strn = ''
buffering  = False

def eol():
  global buffering, strn, barcode
  buffering = False
  barcode = strn
  print(strn)
  strn = ''
def getCodeThread():
  global buffering, strn, barcode
  while True:
    try:
      ch = fp.read(8)
      if(ch):
        code = codeTranslate(ch)
        if code!='EOL' and len(strn)<=30:
          buffering = True
          strn = strn+code
        else:
          eol()
      else:
        if(buffering):
          eol()
        time.sleep(1)
    except Exception as e:
      print('except')
      if(buffering):
          eol()
    finally:
      pass
if __name__ == '__main__':
  getCodeThread()