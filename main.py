import customtkinter as ctk
from settings import *
from PIL import Image, ImageTk
from datetime import date
import sqlite3
from widgets.Widgets import Widgets
from widgets.WindowSlideBooks import WindowSlideBooks
import darkdetect
try:
    from ctypes import wintypes, byref, sizeof, c_int, windll
except:
    print('Não foi possível importar a biblioteca ctypes.')
    pass

class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=(WHITE, BLACK_BACKGROUND))
        self.title('')
        self.configure(fg=BLACK)
        # iniciar tela no centro
        widht_screen = self.winfo_screenwidth() 
        height_screen = self.winfo_screenheight()
        x = int(widht_screen/2 - int(APP_SIZE[0])/2)
        y = int(height_screen/2 - int(APP_SIZE[1])/2)
        self.geometry(f'{APP_SIZE[0]}x{APP_SIZE[1]}+{x}+{y}')
        
        # if darkdetect.isLight():
        #     ctk.set_appearance_mode('dark')
        
        
        
        self.iconbitmap("images/favicon.ico")
        self.resizable(False, False)
        
        self.create_bd()
        
        # widgets
        Widgets(self)
        
        
        self.mainloop()
    
    def title_bar_color(self):
        try:
            
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATRIBUTE = 35
            # dark gray
            COLOR = 0x00000000
            windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATRIBUTE, byref(c_int(COLOR)), sizeof(c_int(COLOR)))
            
            
        except:
            print('Não foi possível alterar a cor da barra de título.')
            pass
    
    def create_bd(self):
        # criar banco de dados para armazenar os livros
        conn = sqlite3.connect('database.db')
        
        # criar cursor
        cursor = conn.cursor()
        
        # Criar uma tabela
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS livros (
                id INTEGER PRIMARY KEY,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL,
                ano TEXT,
                nota INTEGER,
                status INTEGER NOT NULL
                
            )
        ''')
        
        # Fechar a conexão
        conn.close()


if __name__ == '__main__':
    App()