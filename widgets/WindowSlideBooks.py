import customtkinter as ctk
from settings import *


class WindowSlideBooks():
    
    bool_window = False # variável de classe
    
    def __init__(self, parent):

        # layout
        parent.columnconfigure(0, weight=1, uniform='a')
        parent.rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1, uniform='a')
        
        # fonts
        font = ctk.CTkFont(family=FONT, size=24, weight='bold')
        font_buttons = ctk.CTkFont(family=FONT, size=24, weight='bold')
        
        
        # frames
        main_frame = ctk.CTkFrame(parent, fg_color='transparent')
        main_frame.grid(column=0, row=0, rowspan=10, sticky='nsew', pady=0, padx=0)
        
        main_frame.columnconfigure(0, weight=1, uniform='b')
        main_frame.rowconfigure(0, weight=1, uniform='b')
        main_frame.rowconfigure(1, weight=9, uniform='b')
        main_frame.rowconfigure(2, weight=1, uniform='b')
        
        top_frame = ctk.CTkFrame(main_frame, fg_color=LIGHT_BLUE, corner_radius=20)
        top_frame.grid(column=0, row=0, sticky='nsew', pady=5, padx=5)
        

        # text top
        text_top = ctk.CTkLabel(master=top_frame, text='Meus Livros', text_color=BLACK, font=font,
                                fg_color='transparent',
                                 corner_radius=20)
        # text_top.grid(column=0,row=0, sticky='new', pady=0, padx=0)
        text_top.place(relx=0.5, rely=0.5, anchor='center')
        
        
        # back button
        # voltar = ctk.CTkButton(master=main_frame, text='>>', 
        #                         command= parent.animate,
        #                         fg_color=LIGHT_BLUE,
        #                         text_color=BLACK,
        #                         font=font_buttons,
        #                         width=5, height=20,
        #                         corner_radius=20)
        # voltar.pack(padx=5, pady=0, expand=True, fill='both')
        voltar = ctk.CTkLabel(master=top_frame, text='>>', text_color=BLACK, font=font,
                                fg_color='transparent',
                                 corner_radius=20)
        # voltar.grid(column=0, row=0, sticky='nw', pady=0, padx=10)
        voltar.place(relx=0.05, rely=0.5, anchor='center')
        
        # add book button
        from .WindowAddBooks import WindowAddBooks
        add_book = ctk.CTkButton(master=main_frame, text='+', 
                                command=WindowAddBooks,
                                fg_color=LIGHT_BLUE,
                                text_color=BLACK,
                                font=font_buttons,
                                corner_radius=100)
        add_book.grid(column=0, row=9, columnspan=9, sticky='s', pady=5)