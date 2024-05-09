import tkinter
from tkinter import filedialog

import soundEncrypt
import customtkinter
import ctkutilities

# GUI setup
infile = ''
outfile = ''

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        container = customtkinter.CTkFrame(self)
        container.pack()
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        container.configure(fg_color='black')

        self.frames = {}
        for F in (Encrypt, Decrypt, HomePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame('HomePage')


    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.lift()



class HomePage(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.encrypt_button = customtkinter.CTkButton(self, command=lambda: controller.show_frame('Encrypt'), text='Encrypt', width=350)
        self.encrypt_button.grid(row=0, column=0, padx=5, pady=5, sticky='NSEW')

        self.decrypt_button = customtkinter.CTkButton(self, command=lambda: controller.show_frame('Decrypt'), text='Decrypt', width=350)
        self.decrypt_button.grid(row=1, column=0, padx=5, pady=5, sticky='NSEW')

        self.exit_button = customtkinter.CTkButton(self, command=self.destroy, text='Quit', width=350)
        self.exit_button.grid(row=2, column=0, padx=5, pady=5, sticky='NSEW')

        self.configure(height=100)



class Encrypt(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)

        self.controller = controller

        self.configure(height=100)


class Decrypt(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.choose_file_button = customtkinter.CTkButton(self, command=self.select_infile, text='Choose File', width=350)
        self.choose_file_button.grid(row=0, column=0, padx=5, pady=5)

        self.choose_location_button = customtkinter.CTkButton(self, command=self.select_outfile,
                                                              text='Choose Output Location', width=350)
        self.choose_location_button.grid(row=1, column=0, padx=5, pady=5)

        self.start_button = customtkinter.CTkButton(self, text='Start', command=lambda:soundEncrypt.decrypt(infile, outfile),
                                                    width=350)
        self.start_button.grid(row=2, column=0, padx=5, pady=5, sticky='NSEW')

        self.configure(height=100)

    def select_infile(self):
        global infile
        infile = filedialog.askopenfilename()

    def select_outfile(self):
        global outfile
        outfile = filedialog.asksaveasfilename(defaultextension='.txt')


if __name__ == '__main__':
    app = App()
    app.mainloop()
