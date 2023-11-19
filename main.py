import customtkinter as ctk
from settings import *
from PIL import Image, ImageTk
from datetime import date
import sqlite3
from widgets.Widgets import Widgets

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('')
        # iniciar tela no centro
        widht_screen = self.winfo_screenwidth() 
        height_screen = self.winfo_screenheight()
        x = int(widht_screen/2 - int(APP_SIZE[0])/2)
        y = int(height_screen/2 - int(APP_SIZE[1])/2)
        self.geometry(f'{APP_SIZE[0]}x{APP_SIZE[1]}+{x}+{y}')
    
        
        #self.iconbitmap('empty.ico')
        self.resizable(False, False)
        
        self.create_bd()
        
        # widgets
        Widgets(self)
        
        self.mainloop()
    
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
                autor TEXT NOT NULL
            )
        ''')
        
        # Fechar a conexão
        conn.close()


if __name__ == '__main__':
    App()