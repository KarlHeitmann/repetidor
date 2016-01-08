import subprocess, time
import Parser

PROGRAMA = ['/usr/bin/gnuplot']
NOMBRE_DESTINO = "respaldo"
LIMITE = 100
class Simulador:
    def __init__(self):
        self.gnuplot=subprocess.Popen(PROGRAMA,stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        self.data_parser=Parser.Parser("SIMULAR")
        self.f = open(NOMBRE_DESTINO, 'r')
        self.n_data = 0
    def run(self):
        cuenta_linea=0
        for line in self.f:
            if ((cuenta_linea % 4)==1):
                self.data_parser.append(line)
                print type(self.data_parser["BAT"])
                print self.data_parser["BAT"]
                print ord(self.data_parser["BAT"][-2])
                if self.n_data == 100:
                    self.plot()
                self.n_data += 1
            cuenta_linea += 1
        self.f.close()
    def plot(self):
        frase = "plot '-' using 1:2\n"
        print >>self.gnuplot.stdin, frase
        data = self.data_parser.get_all("BAT")
        for i in range(self.n_data):
            frase = str(i) + " " + str(ord(data[i][-2]))
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
