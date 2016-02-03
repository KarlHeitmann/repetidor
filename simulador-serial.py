import os
import subprocess, time
import Parser
import Interfaz

PROGRAMA = ['/usr/bin/gnuplot']
NOMBRE_DESTINO = "DATA1.txt"
LIMITE = 100

OPCIONES_MENU = ['1', '2', '3', '4', '5', '6', '7', '8',
            '9', 'a']
HASH_MENU = {'1':"SYSTEM", '2':"START", '3':"CONNECT", '4':"PERF",
        '5':"PWR", '6':"PERV", '7':"PFR", '8':"RED", '9':"BAT", 'a':"ANG",
        'b':"HTH"}
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
    def plot(self, tipo):
        frase = "plot '-' using 1:2\n"
        print >>self.gnuplot.stdin, frase
        data = self.data_parser.get_all(tipo)
        for i in range(self.n_data):
            frase = str(i) + " " + str(ord(data[i][-2]))
            print >>self.gnuplot.stdin, frase
        frase = "e\n"
        print >>self.gnuplot.stdin, frase

        self.data_parser[tipo]
def menu():
    os.system('clear')
    print "(1) SYSTEM"
    print "(2) START"
    print "(3) CONNECT"
    print "(4) FRECUENCIA"
    print "(5) POTENCIA"
    print "(6) VOLTAJE"
    print "(7) PFR"
    print "(8) RED"
    print "(9) BATERIA"
    print "(a) COSENO FI"
    print "(b) ALTURA"
    resp = raw_input("Escoja su opcion para analizar? ")
    while(not(resp in OPCIONES_MENU)):
        print "OPCION NO DISPONIBLE"
        resp = raw_input("Escoja su opcion para analizar")
    return resp

def run():
    sim = Simulador()
    sim.run()
    todo_data = sim.data_parser
    while(True):
        resp = menu()
        tipo = raw_input("[G]raficar o [E]nviar? ")
        if tipo != "g":
            data=todo_data.get_all(HASH_MENU[resp])
            for i in range(len(data)):
                print "ENVIANDO"
                print str(data[i])
                os.system("ruby comunicador.rb " + str(ord(data[i][-2])))
                time.sleep(5)
        else:
            sim.plot(HASH_MENU[resp])
            raw_input("<enter> para continuar")

def run_curses():
    sim = Simulador()
    print "DSADAS"
    interfaz = Interfaz.Interfaz()
    interfaz.build()
    resp = interfaz.menu()
    interfaz.show("simulando..." + resp)
    sim.run()
    print str(sim.data_parser.get_all("SYSTEM"))
    interfaz.show(str(sim.data_parser.get_all("SYSTEM")))


if __name__ == '__main__':
    resp = raw_input('Iniciar modo curses? [s/n] ')
    if resp == 's':
        run_curses()
    else:
        run()
