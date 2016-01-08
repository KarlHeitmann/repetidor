import curses

TAMANO_COMMANDS = 10
'''
class Data(curses):
    def __init__(self):
        pass
'''

class Interfaz:
    def __init__(self):
        #Inicia pantalla, no devuelve eco teclado, no requiere tecla <intro>, habilita a curses manejar las teclas especiales
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self.stdscr.keypad(True)
    def build(self):
        self.stdscr.addstr(0,0, "Hola")
        self.data = curses.newwin(curses.LINES-TAMANO_COMMANDS, curses.COLS, 0,0)
        self.command = curses.newwin(TAMANO_COMMANDS, curses.COLS, curses.LINES-TAMANO_COMMANDS, 0)
        self.data.border(0)
        self.command.addstr(0,0,"COMANDOS", curses.A_BOLD)
        self.data.refresh()
        self.command.refresh()
        self.command.getkey()
    def ask_data(self):
        pass
        
    def __del__(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()

def run():
    window = Interfaz()
    window.build()

if __name__ == '__main__':
    run()
