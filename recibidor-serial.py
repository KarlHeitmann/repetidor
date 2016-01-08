'''
Apuntes: en la linea 238 de datatrans.c empieza a imprimir los caracteres
 manda unsigned int de 3 espacios (si es mas largo los corta), separados por
 el caracter '*'. Salvo los indicados a la derecha del nombre de variable. Recordar
 que:
 %3u -> imprime 3 caracteres del unsigned int, si es mas corto, hace un pad con espacios
 blancos
 %7lu -> 7 caracteres de long unsigned int

Se trata de las variables siguientes (11 datos)

SISTEM
START
CONECT
SUMA = PERF5+PERF4...+PERF1 %7lu
SUMA = PWR5 + ... + PWR1 %6lu
SUMA = PERV5 + ... + PERV1 %7lu
SUMA = PFR5 + ... + PFR1 %5lu
SUMA = RED5 + ... + RED1 %4lu
SUMA = BAT5 + ... + BAT1 %4lu
SUMA = ANG5 + ... + ANG1 %4lu
SUMA = HTH5 + ... + HTH1 %4lu


CARACTERES ENVIADOS: 62
'''

import serial
data_parser = {"SYSTEM":0, "START":0, "CONECT":0, "PERF":0,
        "PWR":0, "PERV":0, "PFR":0, "RED":0, "BAT":0, "ANG":0,
        "HTH":0,}
MODO=1

ser = serial.Serial ("/dev/ttyAMA0", timeout=0.5) #Open named port 
ser.baudrate = 4800                  #Set baud rate to 9600
while(True):
    ser.flush()
    cadena = ''
    data = ser.read(100)
    data_hex = data.encode('hex')
    data_parser["SYSTEM"] = data[0:3]
    data_parser["START"] = data[4:7]
    data_parser["CONECT"] = data[8:11]
    data_parser["PERF"] = data[12:19]
    data_parser["PWR"] = data[20:26]
    data_parser["PERV"] = data[27:34]
    data_parser["PFR"] = data[35:40]
    data_parser["RED"] = data[41:45]
    data_parser["BAT"] = data[46:50]
    data_parser["ANG"] = data[51:55]
    data_parser["HTH"] = data[56:60]
    print len(data)
    print data_hex
    print len(data_hex)
    print data_parser
    

#ser.write(data)                      #Send back the received data
ser.close()   
