import subprocess
import time

programa = ['/usr/bin/gnuplot']

p=subprocess.Popen(programa,stdin=subprocess.PIPE,stdout=subprocess.PIPE)

frase="plot '-' using 1:2\n"
print >>p.stdin, frase
frase="1 0\n"
print >>p.stdin, frase
frase="2 9\n"
print >>p.stdin, frase
frase="3 2\n"
print >>p.stdin, frase
frase="4 3\n"
print >>p.stdin, frase
frase="5 5\n"
print >>p.stdin, frase
frase="6 7\n"
print >>p.stdin, frase
frase="7 2\n"
print >>p.stdin, frase
frase="e\n"
print >>p.stdin, frase

time.sleep(5)
frase="exit \n"
print >>p.stdin, frase
