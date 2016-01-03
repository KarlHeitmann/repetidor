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
import subprocess, time

PROGRAMA = ['/usr/bin/gnuplot']
NOMBRE_DESTINO = "respaldo"
LIMITE = 100
class Simulador:
    def __init__(self):
        self.gnuplot=subprocess.Popen(PROGRAMA,stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        self.data_parser={}
        self.f = open(NOMBRE_DESTINO, 'r')
        self.n_data = 0
    def run(self):
        cuenta_linea=0
        for line in self.f:
            if ((cuenta_linea % 4)==1):
                self.data_parser["SYSTEM"] = line[0*2:2*3].decode('hex')
                self.data_parser["START"] = line[4*2:2*7].decode('hex')
                self.data_parser["CONECT"] = line[8*2:2*11].decode('hex')
                self.data_parser["PERF"] = line[12*2:2*19].decode('hex')
                self.data_parser["PWR"] = line[20*2:2*26].decode('hex')
                self.data_parser["PERV"] = line[27*2:2*34].decode('hex')
                self.data_parser["PFR"] = line[35*2:2*40].decode('hex')
                self.data_parser["RED"] = line[41*2:2*45].decode('hex')
                self.data_parser["BAT"] = line[46*2:2*50].decode('hex')
                self.data_parser["ANG"] = line[51*2:2*55].decode('hex')
                self.data_parser["HTH"] = line[56*2:2*60].decode('hex')
                print type(self.data_parser["BAT"])
                print self.data_parser["BAT"]
                print ord(self.data_parser["BAT"][-2])
                if self.n_data == 100:
                    self.plot()
                self.n_data += 1
            cuenta_linea += 1
    def plot(self):
        frase = "plot '-' using 1:2\n"
        print >>self.gnuplot.stdin, frase
        for i in range(self.n_data):
            frase = str(i) + " " + self.data_parser["SYSTEM"]
            print >>self.gnuplot.stdin, frase
        frase = "e\n"
        print >>self.gnuplot.stdin, frase
        time.sleep(5)

        self.data_parser["SYSTEM"]

def run():
    sim = Simulador()
    sim.run()

if __name__ == '__main__':
    run()
