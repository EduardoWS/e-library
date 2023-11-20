import customtkinter as ctk
from settings import *
import sqlite3


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
        main_frame = ctk.CTkFrame(parent, fg_color=DARK_GRAY, )
        main_frame.grid(column=0, row=0, rowspan=10, sticky='nsew', pady=0, padx=0)
        
        main_frame.columnconfigure(0, weight=1, uniform='b')
        main_frame.rowconfigure(0, weight=1, uniform='b')
        main_frame.rowconfigure(1, weight=9, uniform='b')
        main_frame.rowconfigure(2, weight=1, uniform='b')
        
        top_frame = ctk.CTkFrame(main_frame, fg_color=LIGHT_BLUE, corner_radius=20)
        top_frame.grid(column=0, row=0, sticky='nsew', pady=5, padx=5)
        
        middle_frame = ctk.CTkFrame(main_frame, fg_color='transparent', )
        middle_frame.grid(column=0, row=1, sticky='nsew', pady=5, padx=5)
        middle_frame.columnconfigure(0, weight=1, uniform='c')
        middle_frame.rowconfigure(0, weight=1, uniform='c')
        middle_frame.rowconfigure(1, weight=14, uniform='c')
        
        segmented_frame = ctk.CTkFrame(middle_frame, fg_color= 'transparent', corner_radius=20)
        segmented_frame.grid(column=0, row=0, sticky='nsew', pady=0, padx=0)
        
        scroll_frame = ctk.CTkScrollableFrame(middle_frame, fg_color=BLACK, corner_radius=20)
        scroll_frame.grid(column=0, row=1, sticky='nsew', pady=10, padx=10)
        scroll_frame.columnconfigure(0, weight=1, uniform='d')
        scroll_frame.rowconfigure((0,1,2,3,4,5,6,7), weight=1, uniform='d')
        
        self.scroll_frame = scroll_frame
        

        # text top
        text_top = ctk.CTkLabel(master=top_frame, text='Meus Livros', text_color=BLACK, font=font,
                                fg_color='transparent',
                                 corner_radius=20)
        # text_top.grid(column=0,row=0, sticky='new', pady=0, padx=0)
        text_top.place(relx=0.5, rely=0.5, anchor='center')
        
        
        # back = ctk.CTkLabel(master=top_frame, text='>>', text_color=BLACK, font=font,
        #                         fg_color='transparent',
        #                          corner_radius=20)
        # back.place(relx=0.05, rely=0.5, anchor='center')
        
       
        
        
        
        # segmented button
        font_seg = ctk.CTkFont(family=FONT, size=15, weight='bold')
        segmented_button = ctk.CTkSegmentedButton(master=segmented_frame, corner_radius=20,
                                                  values=['Todos', 'Lidos', 'Não Lidos'],
                                                  border_width=5,
                                                  selected_color=GRAY, text_color=LIGHT_BLUE, font=font_seg,
                                                  unselected_color=BLACK, fg_color=BLACK, text_color_disabled=LIGHT_BLUE,
                                                  selected_hover_color=GRAY, unselected_hover_color=GRAY,
                                                  command=self.segmented_button_callback)
        segmented_button.set('Todos')
        segmented_button.place(relx=0.5, rely=0.5, anchor='center')
        # segmented_button.configure(state='disabled')
        # segmented_button.grid(column=0, row=0, sticky='nsew', pady=0, padx=0)
        
        
        
        
        self.show_books(scroll_frame)
        
       
        
        
        
        # add book button
        from .WindowAddBooks import WindowAddBooks
        add_book = ctk.CTkButton(master=main_frame, text='+', 
                                command=lambda: WindowAddBooks(scroll_frame),
                                fg_color=LIGHT_BLUE,
                                text_color=BLACK,
                                font=font_buttons,
                                width=50, height=50,
                                corner_radius=100)
        # add_book.grid(column=0, row=2, columnspan=9, sticky='ns', pady=7)
        add_book.place(relx=0.5, rely=0.9425, anchor='center')
        
        
        
    def segmented_button_callback(self, value):
        if value == 'Todos':
            self.show_books(self.scroll_frame, filtro=None)
        elif value == 'Lidos':
            self.show_books(self.scroll_frame, filtro=1)
        elif value == 'Não Lidos':
            self.show_books(self.scroll_frame, filtro=0)
        
        
    
    def show_books(self, scroll_frame, filtro=None):
        # limpar frame
        for widget in scroll_frame.winfo_children():
            widget.destroy()
        
        
        # mostrar livros cadastrados no banco de dados
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        if filtro == None:
            cursor.execute('SELECT * FROM livros ORDER BY id DESC')
        else:
            cursor.execute(f'SELECT * FROM livros WHERE status = {filtro} ORDER BY id DESC')
        livros = cursor.fetchall()
        conn.close()
        
        font = ctk.CTkFont(family=FONT, size=18)
        for livro in livros:
            if livro[3] == None:
                # ctk.CTkLabel(scroll_frame, text=f'{livro[1]} - {livro[2]}', font=font, 
                #              height=40,
                #             text_color=WHITE, fg_color=DARK_GRAY, corner_radius=20).pack(pady=10, padx=10, 
                #                                                                          anchor='w', fill='y', 
                #                                                                          )
            else:
                # ctk.CTkLabel(scroll_frame, text=f'{livro[1]} - {livro[2]}', font=font, 
                #              height=40,
                #             text_color=LIGHT_BLUE, fg_color=DARK_GRAY, corner_radius=20).pack(side='left', pady=10, padx=10, 
                #                                                                               anchor='w', fill='y',
                #                                                                               )
                # ctk.CTkLabel(scroll_frame, text=f'{livro[3]}', font=font, height=40,
                #             text_color=LIGHT_BLUE, fg_color=DARK_GRAY, corner_radius=20).pack(side='left', pady=10, padx=0, 
                #                                                                               anchor='w', fill='y',
                #                                                                               )
                nota = " ★ " * livro[4]
                
                # ctk.CTkLabel(scroll_frame, text=f'{nota}', font=font, height=40,
                #             text_color=LIGHT_BLUE, fg_color=DARK_GRAY, corner_radius=20).pack(side='left', pady=10, padx=10, 
                #                                                                               anchor='w', fill='y',
                #                                                                               )
        
        
    
    
            
            