import customtkinter as ctk
from settings import *

class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master = parent)
        

        # general attributes 
        self.start_pos = start_pos 
        self.end_pos = end_pos 
        self.width = abs(start_pos - end_pos)
        
        self.configure(fg_color=DARK_GRAY)

        # animation logic
        self.pos = self.start_pos
        self.in_start_pos = True

        # layout
        self.place(relx = self.start_pos, rely = 0, relwidth = self.width, relheight = 1)
        

    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()

    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos -= 0.05
            self.place(relx = self.pos, rely = 0, relwidth = self.width, relheight = 1)
            self.after(16, self.animate_forward)
        else:
            
            self.in_start_pos = False
            

    def animate_backwards(self):
        if self.pos < self.start_pos:
            self.pos += 0.05
            self.place(relx = self.pos, rely = 0, relwidth = self.width, relheight = 1)
            self.after(16, self.animate_backwards)
        else:
            self.in_start_pos = True
