from PIL import Image
import customtkinter as ctk
from settings import *
from .SlidePanel import *
from .WindowAddBooks import WindowSlideBooks

class Widgets():
   
    def __init__(self, parent):
        
        # layout
        parent.columnconfigure(0, weight=1, uniform='a')
        parent.columnconfigure(1, weight=3, uniform='a')
        parent.rowconfigure((0,1,2,3,4,5,6), weight=1, uniform='a')
        
        self.frames(parent)
        
    def frames(self, parent):
        # fonts
        font = ctk.CTkFont(family=FONT, size=MAIN_TEXT_SIZE, weight='bold')
        font_buttons = ctk.CTkFont(family=FONT, size=24, weight='bold')
        # frames
        main_frame = ctk.CTkFrame(parent, fg_color=LIGHT_BLUE, corner_radius=20)
        main_frame.grid(column=1, row=0, rowspan=2, sticky='new', padx=80, pady=40)
        
        
        text_logo = ctk.CTkLabel(master=main_frame, text='e-Library', text_color=BLACK, font=font,
                                 corner_radius=20)
        text_logo.pack(expand=True, fill='both', padx=30, pady=30)
        


        # buttons
        frame_buttons = ctk.CTkFrame(master=parent, fg_color=(WHITE, GRAY))
        frame_buttons.grid(column=0, row=0, rowspan=7, sticky='nsew')
        frame_buttons.columnconfigure(0, weight=1, uniform='f')
        frame_buttons.rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1, uniform='f')
        
        self.parent = parent
        self.frame_buttons = frame_buttons
        
        
        
        self.flag_selected_button = False
        animated_panel = SlidePanel(self.parent, 1.0, 0.25)
        
        
        # button1
        self.button1 = ctk.CTkButton(master=frame_buttons, text=' Meus Livros', 
                                command= lambda: self.slide_panel(animated_panel),
                                border_spacing=10,
                                fg_color='transparent',
                                text_color=(BLACK, LIGHT_BLUE),
                                hover_color=(LIGHT_BLUE, BLACK),
                                font=font_buttons,
                                corner_radius=0,
                                anchor='w',
                                #image=book_ctk
                                )
        self.button1.grid(column=0, row=2, sticky='ew')
        #button1.place(relx=0.5, rely=0.10, relwidth = 1, relheight = 0.1, anchor='center')
       
        
        
        # button2
        button2 = ctk.CTkButton(master=frame_buttons, text=' Lista de Desejos', 
                                fg_color='transparent',
                                border_spacing=10,
                                text_color=(BLACK, LIGHT_BLUE),
                                hover_color=(LIGHT_BLUE, BLACK),
                                font=font_buttons,
                                corner_radius=0,
                                anchor='w',
                                #image=money_ctk
                                )
        button2.grid(column=0, row=3, sticky='ew')
        #button2.place(relx=0.5, rely=0.25, relwidth = 1, relheight = 0.1, anchor='center')
        
 
        

        # button3
        button3 = ctk.CTkButton(master=frame_buttons, text=' Meta de Leitura', 
                                fg_color='transparent',
                                border_spacing=10,
                                text_color=(BLACK, LIGHT_BLUE),
                                hover_color=(LIGHT_BLUE, BLACK),
                                font=font_buttons,
                                corner_radius=0,
                                anchor='w',
                                #image=pin_ctk
                                )
        button3.grid(column=0, row=4, sticky='ew')
        #button3.place(relx=0.5, rely=0.40, relwidth = 1, relheight = 0.1, anchor='center')
        
        # button4
        button4 = ctk.CTkButton(master=frame_buttons, text='Creditos', 
                                fg_color=LIGHT_BLUE,
                                text_color=BLACK,
                                font=font_buttons,
                                )
        #button4.place(relx=0.5, rely=0.9, relwidth = 1, relheight = 0.1, anchor='center')
        
    def slide_panel(self, animated_panel):
        WindowSlideBooks(animated_panel)
        animated_panel.animate()
        if not self.flag_selected_button:
            self.button1.configure(fg_color=BLACK)
            self.flag_selected_button = True
        else:
            self.button1.configure(fg_color='transparent')
            self.flag_selected_button = False
    
    