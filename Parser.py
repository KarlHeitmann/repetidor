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

NOMBRE_DESTINO = "DATA1.txt"

class Parser:
    def __init__(self, modo):
        self.modo = modo
        self.data = {"SYSTEM":[], "START":[], "CONECT":[], "PERF":[],
        "PWR":[], "PERV":[], "PFR":[], "RED":[], "BAT":[], "ANG":[],
        "HTH":[]}
    def append(self, raw):
        if (self.modo == "SIMULAR"):
            raw = raw.split('*')
            self.data["SYSTEM"].append(raw[0])
            self.data["START"].append(raw[1])
            self.data["CONECT"].append(raw[2])
            self.data["PERF"].append(raw[3])
            self.data["PWR"].append(raw[4])
            self.data["PERV"].append(raw[5])
            self.data["PFR"].append(raw[6])
            self.data["RED"].append(raw[7])
            self.data["BAT"].append(raw[8])
            self.data["ANG"].append(raw[9])
            self.data["HTH"].append(raw[10])
        if (self.modo == "SIMULAR_GARBAGE"):
            self.data["SYSTEM"].append(raw[0*2:2*3].decode('hex'))
            self.data["START"].append(raw[4*2:2*7].decode('hex'))
            self.data["CONECT"].append(raw[8*2:2*11].decode('hex'))
            self.data["PERF"].append(raw[12*2:2*19].decode('hex'))
            self.data["PWR"].append(raw[20*2:2*26].decode('hex'))
            self.data["PERV"].append(raw[27*2:2*34].decode('hex'))
            self.data["PFR"].append(raw[35*2:2*40].decode('hex'))
            self.data["RED"].append(raw[41*2:2*45].decode('hex'))
            self.data["BAT"].append(raw[46*2:2*50].decode('hex'))
            self.data["ANG"].append(raw[51*2:2*55].decode('hex'))
            self.data["HTH"].append(raw[56*2:2*60].decode('hex'))
        elif (self.modo == "RECIBIR"):
            self.data["SYSTEM"] = raw[0:3]
            self.data["START"] = raw[4:7]
            self.data["CONECT"] = raw[8:11]
            self.data["PERF"] = raw[12:19]
            self.data["PWR"] = raw[20:26]
            self.data["PERV"] = raw[27:34]
            self.data["PFR"] = raw[35:40]
            self.data["RED"] = raw[41:45]
            self.data["BAT"] = raw[46:50]
            self.data["ANG"] = raw[51:55]
            self.data["HTH"] = raw[56:60]
    def __getitem__(self, key):
        return self.data[key][-1]
    def get_all(self, key):
        return self.data[key]
if __name__ == '__main__':
    data = Parser("SIMULAR")
    f = open(NOMBRE_DESTINO, 'r')
    for line in f:
        data.append(line)
    print data.get_all("SYSTEM")
    print data.get_all("START")
    print data.get_all("CONECT")
    print data.get_all("PERF")
    print data.get_all("PERV")
    print data.get_all("PFR")
    print data.get_all("RED")
    print data.get_all("BAT")
    print data.get_all("ANG")
    print data.get_all("HTH")



























