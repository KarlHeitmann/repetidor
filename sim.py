import os
import subprocess, time
import Parser
import Interfaz
import json

NOMBRE_DESTINO = "DATA1.txt"
LIMITE = 100

OPCIONES_MENU = ['1', '2', '3', '4', '5', '6', '7', '8',
            '9', 'a', 'b']
HASH_MENU = {'1':"SYSTEM", '2':"START", '3':"CONNECT", '4':"PERF",
        '5':"PWR", '6':"PERV", '7':"PFR", '8':"RED", '9':"BAT", 'a':"ANG",
        'b':"HTH"}
class Simulador:
    def __init__(self):
        self.data_parser=Parser.Parser("SIMULAR")
        self.f = open(NOMBRE_DESTINO, 'r')
        self.n_data = 0
    def run(self):
        cuenta_linea=0
        for line in self.f:
            self.data_parser.append(line)
            cuenta_linea += 1
            paquete = json.dumps(self.data_parser.get_last())
            callstr = "ruby comunicador.rb " + '\'' + paquete + '\''
            os.system(callstr)
            time.sleep(5)
        self.f.close()
def run():
    sim = Simulador()
    sim.run()
    
    #os.system("ruby comunicador.rb " + str(ord(data)))
    #time.sleep(5)

if __name__ == '__main__':
    run()
