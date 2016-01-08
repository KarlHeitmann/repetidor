import curses

TAMANO_COMMANDS = 10

MARGIN_LEFT = 5
MARGIN_TOP = 3
DIVISION_MENU_PALABRAS = 20
DIVISION_MENU_MARGEN_TOP = 1

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
        self.data_y=MARGIN_TOP
        self.data_x=MARGIN_LEFT
        self.command_y=MARGIN_TOP
        self.command_x=MARGIN_LEFT
    def build(self):
        self.stdscr.addstr(0,0, "Hola")
        self.data = curses.newwin(curses.LINES-TAMANO_COMMANDS, curses.COLS, 0,0)
        self.command = curses.newwin(TAMANO_COMMANDS, curses.COLS, curses.LINES-TAMANO_COMMANDS, 0)
        self.data.border(0)
        self.data.refresh()
        self.paint_commands()
        self.command.getkey()
    def menu(self):
        self.paint_commands()
        self.command.addstr(DIVISION_MENU_MARGEN_TOP, MARGIN_LEFT, "Escoja su opcion para analizar.")
        self.command.addstr(DIVISION_MENU_MARGEN_TOP + 2,MARGIN_LEFT, "(1) SYSTEM")
        self.command.addstr(DIVISION_MENU_MARGEN_TOP + 3,MARGIN_LEFT, "(3) START")
        self.command.addstr(DIVISION_MENU_MARGEN_TOP + 4,MARGIN_LEFT, "(4) CONNECT")
        self.command.addstr(DIVISION_MENU_MARGEN_TOP + 5,MARGIN_LEFT, "(5) PERF")
        self.command.addstr(DIVISION_MENU_MARGEN_TOP + 6,MARGIN_LEFT, "(6) POTENCIA")
        self.command.addstr(DIVISION_MENU_MARGEN_TOP + 7,MARGIN_LEFT, "(7) FRECUENCIA")
        self.command.addstr(DIVISION_MENU_MARGEN_TOP + 2,MARGIN_LEFT + DIVISION_MENU_PALABRAS, "(8) RED")
        self.command.addstr(DIVISION_MENU_MARGEN_TOP + 3,MARGIN_LEFT + DIVISION_MENU_PALABRAS, "(9) BATERIA")
        self.command.addstr(DIVISION_MENU_MARGEN_TOP + 4,MARGIN_LEFT + DIVISION_MENU_PALABRAS, "(a) COSENO FI")
        self.command.addstr(DIVISION_MENU_MARGEN_TOP + 5,MARGIN_LEFT + DIVISION_MENU_PALABRAS, "(b) ALTURA")
        self.commands_wait()
    def show(self, texto):
        self.paint_commands()
        self.command.addstr(self.command_y, self.command_x, texto)
        self.commands_wait()
    def get(self, texto):
        self.command.addstr(self.command_y, self.command_x, texto)
    def commands_wait(self):
        self.command.refresh()
        self.command.getkey()
    def paint_commands(self):
        self.command.clear()
        self.command.addstr(0,0,"COMANDOS", curses.A_BOLD)
        self.command.refresh()

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
    window.menu()

if __name__ == '__main__':
    run()
