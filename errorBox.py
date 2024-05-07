from tkinter import Toplevel
import customtkinter

class ErrorMessage(customtkinter.CTkToplevel):
    def __init__(self, error):
        super().__init__()
        self.geometry('150x75')

        self.message = customtkinter.CTkLabel(
            master=None,
            text=error, 
            fg_color = 'transparent',
            width=100,
            justify='left',
            anchor='w')
        self.message.place(x=0,y=0)
        self.message.pack(padx=20, pady=20)

class DisplayBox(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('100x50')
        self.title('Error!')

    def errorMessage(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)
            
        else:
            self.toplevel_window.focus()
