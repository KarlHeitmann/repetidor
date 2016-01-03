import subprocess
import time

#programa = ['/usr/bin/octave']
programa = ['/usr/bin/octave', '-i']

p=subprocess.Popen(programa,stdin=subprocess.PIPE,stdout=subprocess.PIPE)

frase="x=[1 2 3];\n"
print >>p.stdin, frase
frase="y=[1 2 3];\n"
print >>p.stdin, frase
frase="plot(x,y);\n"
print >>p.stdin, frase

time.sleep(5)
frase="exit \n"
print >>p.stdin, frase
