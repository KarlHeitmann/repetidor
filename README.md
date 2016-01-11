# Repetidor

Bienvenido al código fuente del proyecto *repetidor*, el proyecto para simular y hacer pruebas con la información
recolectada a través del puerto RS232, transmitida por un grupo electrógeno.

El proyecto adopta en Github este nombre en clave porque es más corto y además... eso es lo que hace el proyecto: repite
la información guardada en una *sesión de grabación* con el grupo electrógeno.

# Código

## Carpeta *pruebas*

Esta carpeta contiene diferentes archivos que se utilizaron para hacer pruebas básicas en la raspberry pi. La mayoría son archivos de ejemplos descargados de distintos sitios web, por ejemplo: **blink.py**, que hace parpadear un led conectado al pin GPIO 11; **example-curses.py**, que muestra un ejemplo de como usar la librería *ncurses*; **example-pipas.py**, que muestra un ejemplo de como comunicarse con pipas con un proceso hijo *gnuplot*, etc.

## Interfaz.py

Este módulo hace de interfaz con la librería ncurses, es un bosquejo para que uno pueda usar el terminal con esa librería. El problema que hay es que si ocurre un error en tiempo de ejecución utilizando *ncurses*, los mensajes de error no aparecen. Es más difícil depurar un programa que utiliza esta librería

## Parser.py

Al instanciarse, se genera un *hash* que se puede ir llenando con un string de caracteres. La gracia es que el módulo **Parser** por si solo hace todo el trabajo de transformar los datos y clasificarlos según su posición en el string entregado. Después con pasarle una llave como parámetro, la instancia devolverá la información que le corresponde dentro del *hash*

## comunicador.rb

Es un pequeño script en ruby que toma el argumento de entrada y lo envía a la dirección web y al puerto que tiene *hard coded*, la información la manda en formato **POST**

## recibidor-serial.py

Este programa sirve para recibir los datos a través del puerto serial: Cada vez que le llegan datos, los pasa a hexadecimal y muestra en pantalla la información en hexadecimal y bruta, además de introducirla en un *hash* y mostrar ese mismo por pantalla. Uso:
> python recibidor-serial.py > *archivo-de-respaldo*

## respaldo

Es un archivo que contiene 596 líneas, y por cada cuatro líneas tenemos un solo dato, o sea que en este archivo tenemos 149 datos. Éstos se ocupan como fuente de información para el programa *simulador-serial*, descrito más abajo

## simulador-serial.py

Módulo de simulación, si uno responde que si a ejecutar ncurses, la interfaz de usuario cambia. Sin embargo, este modo de funcionamiento aún está en nivel *beta*.

La idea es que al ejecutarse, el proceso ingrese a un *loop infinito* en el cuál cada vez le pregunta al usuario qué hacer: con qué dato trabajar, y luego si debe graficar o enviar los datos que el usuario escogió. 

Los datos con que el simulador trabajará serán los datos recolectados por el *recibidor-serial* y almacenados en el archivo plano de texto *respaldo.* En caso que el usuario quiera graficar los datos, se comunica con el proceso *gnuplot* (utilizamos este programa en lugar de *octave* porque *gnuplot* es más liviano y consume mucho menos recursos que el otro) y le manda la información a graficar. Caso contrario, llama al programa comunicador.rb y le manda como parámetro la información que debe enviar a la página web


