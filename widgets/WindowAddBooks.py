from settings import *
import customtkinter as ctk
from datetime import date
import sqlite3
from .WindowSlideBooks import WindowSlideBooks

       
class WindowAddBooks():
    def __init__(self):
        
        if not WindowSlideBooks.bool_window:
            global extra
            extra = ctk.CTkToplevel()
            extra.title('')
            # iniciar tela no centro
            widht_screen = extra.winfo_screenwidth()
            height_screen = extra.winfo_screenheight()
            x = int(widht_screen/2 - 500/2) + 100
            y = int(height_screen/2 - 400/2)
            extra.geometry(f'500x400+{x}+{y}')
            extra.resizable(False, False)
            # print(extra.attributes())
            extra.attributes('-topmost', 'true') # o topmost faz com que a janela fique sempre em primeiro plano
            
            # layout
            extra.columnconfigure(0, weight=1, uniform='c')
            extra.rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1, uniform='c')
            
           
            
            # frames
            main_frame = ctk.CTkFrame(extra, corner_radius=20, fg_color='transparent')
            main_frame.grid(column=0, row=2, rowspan=8, sticky='nsew', pady=10, padx=10)
            
            main_frame.columnconfigure(0, weight=1, uniform='c')
            main_frame.columnconfigure(1, weight=3, uniform='c')
            main_frame.rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1, uniform='c')
            
            back_ground_frame = ctk.CTkFrame(master=main_frame, fg_color='transparent')
            back_ground_frame.grid(column=0, columnspan=4, row=6, rowspan=4, sticky='nsew')
            back_ground_frame.columnconfigure((0,1,2,3), weight=1, uniform='d')
            back_ground_frame.rowconfigure((0,1,2,3), weight=1, uniform='d')
            
            hide_frame = ctk.CTkFrame(master=main_frame, fg_color=(WHITE, DARK_GRAY))
            hide_frame.columnconfigure(0, weight=1, uniform='d')
            hide_frame.columnconfigure((1,2,3,4,5,6), weight=1, uniform='d')
            hide_frame.rowconfigure((0,1,2), weight=1, )
            
            
            


            
            # widgets
            
            font_top = ctk.CTkFont(family=FONT, size=22, weight='bold')
            text_top = ctk.CTkLabel(master=main_frame, text='Adicionar Livro', text_color=LIGHT_BLUE, font=font_top,)
            text_top.grid(column=0, columnspan=2, row=0, sticky='nsw', pady=5, padx=15)
            
            
            font_label = ctk.CTkFont(family=FONT, size=16, weight='bold')
            font_entry = ctk.CTkFont(family=FONT, size=15)
            
            title_label = ctk.CTkLabel(master=main_frame, text='Título:', text_color=(BLACK, WHITE), font=font_label,
                                    #    fg_color=LIGHT_BLUE,
                                       corner_radius=20)
            title_label.grid(column=0, row=2, sticky='nsw', pady=3, padx=5)
            
            
            title_entry = ctk.CTkEntry(master=main_frame, font=font_entry,
                                       border_color=LIGHT_BLUE, height=20, width=300,
                                       corner_radius=3, border_width=1,
                                       placeholder_text='Digite o título do livro')
           
            title_entry.grid(column=1, columnspan=3, row=2, sticky='nsw', pady=3, padx=5)
            
            
            author_label = ctk.CTkLabel(master=main_frame, text='Autor:', text_color=(BLACK, WHITE), font=font_label,
                                    #    fg_color=LIGHT_BLUE,
                                       corner_radius=20)
            author_label.grid(column=0, row=3, sticky='nsw', pady=3, padx=5)
            author_entry = ctk.CTkEntry(master=main_frame, font=font_entry,
                                       border_color=LIGHT_BLUE, height=20, width=300,
                                       corner_radius=3, border_width=1,
                                       placeholder_text='Digite o nome do autor')
           
            author_entry.grid(column=1, columnspan=3, row=3, sticky='nsw', pady=3, padx=5)
            
            
            
           
            book_readed = ctk.BooleanVar(value=False)
            readed_label = ctk.CTkLabel(master=main_frame, text='Lido:', text_color=(BLACK, WHITE), font=font_label,
                                    #    fg_color=LIGHT_BLUE,
                                       corner_radius=20)
            readed_label.grid(column=0, row=4, sticky='nsw', pady=5, padx=5)
            readed_toggle = ctk.CTkSwitch(master=main_frame, progress_color=LIGHT_BLUE,
                                            text='',
                                            offvalue=False, onvalue=True, variable=book_readed,
                                            command=lambda: self.func_book_readed(book_readed, hide_frame))
          
            readed_toggle.grid(column=1, row=4, pady=5, padx=5, sticky='w')
            
            # separator = ttk.Separator(main_frame, orient='horizontal')
            # separator.grid(column=0, columnspan=4, row=5, sticky='nsew', pady=5, padx=5)
            separator = ctk.CTkLabel(master=main_frame, text='__________________________________________________________',
                                    text_color=DARK_GRAY, font=font_label,
                                    corner_radius=20)
            separator.grid(column=0, columnspan=4, row=5, sticky='nsew', pady=5, padx=5)
            
            year_label = ctk.CTkLabel(master=hide_frame, text='Ano:', text_color=(BLACK, WHITE), font=font_label,
                                #    fg_color=LIGHT_BLUE,
                                corner_radius=20)
           
            year_str = ctk.StringVar(value=str(date.today().year))
            year_entry = ctk.CTkEntry(master=hide_frame, font=font_entry,
                                        border_color=LIGHT_BLUE, height=20, width=100,
                                        corner_radius=3, border_width=1,
                                        textvariable=year_str)
           
            obs_label = ctk.CTkLabel(master=hide_frame, text='*Ano de conclusão da leitura.', 
                                        text_color=(BLACK, WHITE), font=font_entry)
            year_label.grid(column=0, row=0, sticky='nsw', pady=7, padx=0)
            year_entry.grid(column=1, row=0, pady=7, padx=0)
            obs_label.grid(column=2, columnspan=3, row=0, sticky='w', pady=7, padx=10)
            
            # frame_teste = ctk.CTkFrame(master=hide_frame, fg_color=(BLACK, WHITE))
            # frame_teste.grid(column=1, row=0, sticky='nsw', pady=0, padx=0)
            
            review_label = ctk.CTkLabel(master=hide_frame, text='Nota:', text_color=(BLACK, WHITE), font=font_label,
                                        corner_radius=20)
           
            #TODO: Criar um widget para avaliação do livro de 0 a 5
            font_stars = ctk.CTkFont(family=FONT, size=26, weight='bold')
            
            
            
            
            self.button_star1 = ctk.CTkButton(master=hide_frame, text='★', fg_color='transparent',
                                              hover=False,
                                         width=10, height=10,
                                        text_color=LIGHT_BLUE, font=font_stars,
                                        corner_radius=100, command=lambda: self.change_color(star=1))
            self.button_star2 = ctk.CTkButton(master=hide_frame, text='★', fg_color='transparent',
                                              hover=False,
                                         width=10, height=10,
                                        text_color=LIGHT_BLUE, font=font_stars,
                                        corner_radius=100, command=lambda: self.change_color(star=2))
            self.button_star3 = ctk.CTkButton(master=hide_frame, text='★', fg_color='transparent',
                                              hover=False,
                                         width=10, height=10,
                                        text_color=LIGHT_BLUE, font=font_stars,
                                        corner_radius=100, command=lambda: self.change_color(star=3))
            self.button_star4 = ctk.CTkButton(master=hide_frame, text='★', fg_color='transparent',
                                              hover=False,
                                         width=10, height=10,
                                        text_color=LIGHT_BLUE, font=font_stars,
                                        corner_radius=100, command=lambda: self.change_color(star=4))
            self.button_star5 = ctk.CTkButton(master=hide_frame, text='★', fg_color='transparent',
                                              hover=False,
                                        width=10, height=10,
                                        text_color=LIGHT_BLUE, font=font_stars,
                                        corner_radius=100, command=lambda: self.change_color(star=5))
            
            
            review_label.grid(column=0, row=1, sticky='nsw', pady=7, padx=0)
            
            self.change_color()
            
            
            
            
            
            save_button = ctk.CTkButton(master=main_frame, text='Salvar',
                                        fg_color=LIGHT_BLUE,
                                        text_color=BLACK,
                                        font=font_label,
                                        width=90,
                                        command=lambda: self.salvar_livro(title_entry, author_entry),
                                        corner_radius=20)
            save_button.grid(column=2, row=9, sticky='nsew', pady=5, padx=5)
            
            cancel_button = ctk.CTkButton(master=main_frame, text='Cancelar',
                                        fg_color=LIGHT_BLUE,
                                        text_color=BLACK,
                                        font=font_label,
                                        width=70,
                                        corner_radius=20,
                                        command= self.on_window_close)
            cancel_button.grid(column=1, row=9, sticky='nse', pady=5, padx=5)
            

            
    
            
            WindowSlideBooks.bool_window = True
            
            # Adicionando uma função para ser chamada quando a janela é fechada
            extra.protocol("WM_DELETE_WINDOW", self.on_window_close)
            extra.mainloop()
        else:
            # TODO: Emitir um alerta de que a janela já está aberta
            pass
    
    def salvar_livro(self, title_entry, author_entry):
        # Obter os dados do título e autor dos widgets
        titulo = title_entry.get()
        autor = author_entry.get()

        # Verificar se ambos título e autor estão preenchidos
        if titulo and autor:
            # Inserir dados na tabela
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO livros (titulo, autor) VALUES (?, ?)", (titulo, autor))
            
            # # Confirmar as alterações no banco de dados
            conn.commit()
            
            # Fechar a conexão
            conn.close()
            
            # Fechar a janela extra
            self.on_window_close()
    
    
    def change_color(self, star=None):
        
        if star:
            
            self.button_star1.configure(text_color=BLACK)
            self.button_star2.configure(text_color=BLACK)
            self.button_star3.configure(text_color=BLACK)
            self.button_star4.configure(text_color=BLACK)
            self.button_star5.configure(text_color=BLACK)
            if star == 1:
                self.button_star1.configure(text_color=LIGHT_BLUE)
                self.button_star2.configure(text_color=BLACK)
                self.button_star3.configure(text_color=BLACK)
                self.button_star4.configure(text_color=BLACK)
                self.button_star5.configure(text_color=BLACK)
            elif star == 2:
                self.button_star1.configure(text_color=LIGHT_BLUE)
                self.button_star2.configure(text_color=LIGHT_BLUE)
                self.button_star3.configure(text_color=BLACK)
                self.button_star4.configure(text_color=BLACK)
                self.button_star5.configure(text_color=BLACK)
            elif star == 3:
                self.button_star1.configure(text_color=LIGHT_BLUE)
                self.button_star2.configure(text_color=LIGHT_BLUE)
                self.button_star3.configure(text_color=LIGHT_BLUE)
                self.button_star4.configure(text_color=BLACK)
                self.button_star5.configure(text_color=BLACK)
            elif star == 4:
                self.button_star1.configure(text_color=LIGHT_BLUE)
                self.button_star2.configure(text_color=LIGHT_BLUE)
                self.button_star3.configure(text_color=LIGHT_BLUE)
                self.button_star4.configure(text_color=LIGHT_BLUE)
                self.button_star5.configure(text_color=BLACK)
            elif star == 5:
                self.button_star1.configure(text_color=LIGHT_BLUE)
                self.button_star2.configure(text_color=LIGHT_BLUE)
                self.button_star3.configure(text_color=LIGHT_BLUE)
                self.button_star4.configure(text_color=LIGHT_BLUE)
                self.button_star5.configure(text_color=LIGHT_BLUE)
                
        
        self.button_star1.grid(column=1, row=1, sticky='w')
        self.button_star2.grid(column=2, row=1, sticky='w')
        self.button_star3.grid(column=3, row=1, sticky='w')
        self.button_star4.grid(column=4, row=1, sticky='w')
        self.button_star5.grid(column=5, row=1, sticky='w')
            
    
    def func_book_readed(self, book_readed, hide_frame):

        # mostrar
        if book_readed.get():  
            hide_frame.grid(column=0, columnspan=4, row=6, rowspan=3, sticky='nsew', pady=5, padx=5)
            
        # ocultar
        else: 
            hide_frame.grid_forget()
            
            
    def on_window_close(self):
        # Esta função será chamada quando a janela for fechada
        WindowSlideBooks.bool_window = False  # Defina a variável bool_window como False
        global extra
        extra.destroy()  # Destrua a janela Toplevel