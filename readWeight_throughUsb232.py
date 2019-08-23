import serial
import re
from bottle import get,run

@get("/weight")
def weight():
    ser = serial.Serial('/dev/ttyUSB0',9600,timeout = 0.5)
    old = 0;
    pattern = re.compile(r'\d+')
    while(1):
        data = ser.readline().decode();
        if(len(data)<4):
            continue;
        m = pattern.match(data,2)
        if m:
            weight = int(m.group(0))
        else:
            continue
        if(True or old!=weight):
            obj = {"weight":weight,"unit":"g"}
            old=weight
            return(str(obj))
run(host="0.0.0.0",port=8080)