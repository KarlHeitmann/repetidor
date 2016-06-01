#!/usr/bin/env python
      
  
import serial
import time

NOMBRE_DESTINO = "DATA1.txt"

ser = serial.Serial(
          
  port='/dev/ttyAMA0',
  baudrate = 4800,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout=0.5
)

def run():
    f = open(NOMBRE_DESTINO, 'r')
    n_data = 0
    for line in f:
        print len(line)
        print line
        ser.write(line)
        time.sleep(2.5)
    self.f.close()
    

if __name__ == '__main__':
    run()
