import customtkinter as ctk
from settings import *


class WindowSlideBooks():
    
    bool_window = False # variável de classe
    
    def __init__(self, parent):

        # layout
        parent.columnconfigure((0,1,2,3,4,5,6,7,8,9), weight=1,)
        parent.rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1, uniform='a')
        
        
        # frames
        main_frame = ctk.CTkFrame(parent, corner_radius=20, fg_color='transparent')
        main_frame.grid(column=0, row=0, sticky='nsew', pady=0, padx=10)
        
        main_frame.columnconfigure(0, weight=8, uniform='b')
        main_frame.columnconfigure(1, weight=1, uniform='b')
        main_frame.rowconfigure(0, weight=1, uniform='b')
        
        # back_frame = ctk.CTkFrame(main_frame, corner_radius=100, fg_color='transparent')
        # back_frame.grid(column=0, row=0, sticky='ns', pady=0)
        
        font_buttons = ctk.CTkFont(family=FONT, size=24, weight='bold')
        frame_books = ctk.CTkFrame(master=parent, fg_color='transparent', corner_radius=20)
        frame_books.grid(column=0, row=2, rowspan=7, sticky='nswe', padx=15)
        
        frame_add_book = ctk.CTkFrame(master=parent, fg_color='transparent', corner_radius=20)
        frame_add_book.grid(column=0, row=9, sticky='ns', padx=15, pady=10)
        




        # text top
        font = ctk.CTkFont(family=FONT, size=INPUT_FONT_SIZE, weight='bold')
        text_top = ctk.CTkLabel(master=main_frame, text='Meus Livros', text_color=BLACK, font=font,
                                fg_color=LIGHT_BLUE,
                                 corner_radius=20)
        text_top.grid(column=0, row=0, sticky='nsew', pady=0, padx=5)
        
        # back button
        voltar = ctk.CTkButton(master=main_frame, text='>>', 
                                command= parent.animate,
                                fg_color=LIGHT_BLUE,
                                text_color=BLACK,
                                font=font_buttons,
                                corner_radius=100)
        # voltar.pack(padx=5, pady=0, expand=True, fill='both')
        voltar.grid(column=1, row=0, sticky='nsew', pady=0, padx=5)
        
        # add book button
        from .WindowAddBooks import WindowAddBooks
        add_book = ctk.CTkButton(master=frame_add_book, text='+', 
                                command=WindowAddBooks,
                                fg_color=LIGHT_BLUE,
                                text_color=BLACK,
                                font=font_buttons,
                                corner_radius=100)
        add_book.pack(expand=True, fill='both')