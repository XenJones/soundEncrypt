from tkinter import filedialog

import customtkinter

import soundEncrypt

# globals
infile = ''
outfile = ''

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


class Encrypt(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)

        self.controller = controller

        self.configure(height=100, width=400)


class Decrypt(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.configure(height=100, fg_color='black')

        self.choose_file_button = customtkinter.CTkButton(self, command=self.select_infile, text='Choose File')
        self.choose_file_button.grid(row=0, column=0, padx=5, pady=5, sticky='NSEW', columnspan=2)

        self.choose_location_button = customtkinter.CTkButton(self, command=self.select_outfile,
                                                              text='Choose Output Location')
        self.choose_location_button.grid(row=1, column=0, padx=5, pady=5, sticky='NSEW', columnspan=2)

        self.start_button = customtkinter.CTkButton(self, text='Start',
                                                    command=lambda: soundEncrypt.decrypt(infile, outfile))
        self.start_button.grid(row=0, column=2, padx=5, pady=5, sticky='NSEW')

        self.back_button = customtkinter.CTkButton(self, text='Back', command=lambda: self.controller.show_frame('HomePage'))
        self.back_button.grid(row=1, column=2, padx=5, pady=5, sticky='NSEW')



    def select_infile(self):
        global infile
        infile = filedialog.askopenfilename()

    def select_outfile(self):
        global outfile
        outfile = filedialog.asksaveasfilename(defaultextension='.txt')


if __name__ == '__main__':
    app = App()
    app.mainloop()
