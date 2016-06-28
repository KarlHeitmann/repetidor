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
import os, sys
import subprocess, time
import Parser
import Interfaz
import json
data_parser = {"SYSTEM":0, "START":0, "CONECT":0, "PERF":0,
        "PWR":0, "PERV":0, "PFR":0, "RED":0, "BAT":0, "ANG":0,
        "HTH":0,}
MODO=1

ser = serial.Serial ("/dev/ttyAMA0", timeout=2.5) #Open named port 
ser.baudrate = 4800                  #Set baud rate to 9600
data_parser=Parser.Parser("SIMULAR")
while(True):
    ser.flushInput()
    cadena = ''
    data = ser.read(61)
    print data
    print len(data)

    if len(data) != 0:
        try:
            data_parser.append(data)
            #cuenta_linea += 1
            paquete = json.dumps(data_parser.get_last())
            print paquete
            callstr = "ruby comunicador.rb " + '\'' + paquete + '\''
            os.system(callstr)
            print "EXITO"
        except:
            e = sys.exc_info()[0]
            print e
ser.close()   
