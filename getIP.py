import socket

def getIP():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #s.connect(('www.baidu.com',0))
        s.connect(('192.168.0.1',0))
        #s.connect(('255.255.255.1',0))
        ip = s.getsockname()[0]
    except:
        ip = 'x.x.x.x'
    finally:
        s.close()
    return ip

if __name__ == '__main__':
    ip = getIP()
    print(ip)