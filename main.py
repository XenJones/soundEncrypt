from ast import Lambda
from tkinter import filedialog

import customtkinter

import soundEncrypt

import ctkutilities

# globals
infile = None
outfile = None

#gui
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

        self.columnconfigure(0, weight=1)

        self.encrypt_button = customtkinter.CTkButton(self, command=lambda: controller.show_frame('Encrypt'),
                                                      text='Encrypt')
        self.encrypt_button.grid(row=0, column=0, padx=5, pady=5, sticky='NSEW')

        self.decrypt_button = customtkinter.CTkButton(self, command=lambda: controller.show_frame('Decrypt'),
                                                      text='Decrypt')
        self.decrypt_button.grid(row=1, column=0, padx=5, pady=5, sticky='NSEW')

        self.exit_button = customtkinter.CTkButton(self, command=self.quit, text='Quit')
        self.exit_button.grid(row=2, column=0, padx=5, pady=5, sticky='NSEW')

        self.configure(height=100)

def select_infile():
    global infile
    infile = filedialog.askopenfilename(defaultextension='.wav')

def select_outfile(filetype):
    global outfile
    outfile = filedialog.asksaveasfilename(defaultextension=filetype)

class Encrypt(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)

        self.controller = controller

        self.configure(height=100, width=400)

        self.choose_file_button = customtkinter.CTkButton(self, command=lambda: select_outfile('.wav'), text='Choose File')
        self.choose_file_button.grid(row=0, column=0, padx=5, pady=5, sticky='NSEW', columnspan=2)

        self.entry_box = customtkinter.CTkEntry(self, placeholder_text='Enter the message to convert... ')
        self.entry_box.grid(row=2, column=1, padx=5, pady=5, sticky='NSEW', columnspan=2)

        
        self.start_button = customtkinter.CTkButton(self, text='Start',
                                                    command=lambda: self.encrypt(outfile))
        self.start_button.grid(row=0, column=2, padx=5, pady=5, sticky='NSEW')

        self.back_button = customtkinter.CTkButton(self, text='Back', command=lambda: self.controller.show_frame('HomePage'))
        self.back_button.grid(row=1, column=2, padx=5, pady=5, sticky='NSEW')

    def encrypt(self, output_file):

        message = self.entry_box.get()

        if outfile is not None and message is not None:

            try:
                soundEncrypt.encrypt(message, output_file)
            except Exception as e:
                ctkutilities.MessageBox(self, 'Error!', e, 'OK!', True)

        else:
            ctkutilities.MessageBox(self, 'Error!', 'please enter a valid file and file location!', 'OK!', True)



class Decrypt(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.configure(height=100, fg_color='black')

        self.choose_file_button = customtkinter.CTkButton(self, command=select_infile, text='Choose File')
        self.choose_file_button.grid(row=0, column=0, padx=5, pady=5, sticky='NSEW', columnspan=2)

        self.choose_location_button = customtkinter.CTkButton(self, command=lambda: select_outfile('.txt'),
                                                              text='Choose Output Location')
        self.choose_location_button.grid(row=1, column=0, padx=5, pady=5, sticky='NSEW', columnspan=2)

        self.start_button = customtkinter.CTkButton(self, text='Start',
                                                    command=lambda: self.decrypt(infile, outfile))
        self.start_button.grid(row=0, column=2, padx=5, pady=5, sticky='NSEW')

        self.back_button = customtkinter.CTkButton(self, text='Back', command=lambda: self.controller.show_frame('HomePage'))
        self.back_button.grid(row=1, column=2, padx=5, pady=5, sticky='NSEW')

    def decrypt(input_file, output_file, self):
        if infile is not None and outfile is not None:

            try:
                soundEncrypt.decrypt(input_file, output_file)
            except Exception as e:
                ctkutilities.MessageBox(self, 'Error!', e, 'OK!', True)

        else:
            ctkutilities.MessageBox(self, 'Error!', 'please enter a valid file and file location!', 'OK!', True)


if __name__ == '__main__':
    app = App()
    app.mainloop()
