import subprocess, time
import Parser
import Interfaz

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

        self.data_parser["SYSTEM"]

def run():
    sim = Simulador()
    '''
    interfaz = Interfaz()
    interfaz.ask("")
    '''
    print "simulando..."
    sim.run()
    resp = raw_input("graficar?")
    if resp == 'y':
        sim.plot()
    raw_input("<enter> para finalizar")


if __name__ == '__main__':
    run()
