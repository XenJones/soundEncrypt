import soundEncrypt
import customtkinter
import errorBox

# GUI setup

class app(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('400x400')
        self.title('Sound Encrypt')
        self.command(self.mainMenu())

    def mainMenu(self):
        try:
            for i in self.master.winfo_children():
                i.destroy()
        except:
            errorBox.ErrorMessage(69)

        self.encryptButton = customtkinter.CTkButton(self, command = self.encrypt())
        self.encryptButton.grid(row=0, column=0, padx=20, pady=10)
        self.encryptButton.configure(text='Encrypt')

        self.dencryptButton = customtkinter.CTkButton(self, command = self.dencrypt())
        self.dencryptButton.grid(row=1, column=0, padx=20, pady=10)
        self.dencryptButton.configure(text='Dencrypt')

    def encrypt(self):
        try:
            for i in self.master.winfo_children():
                i.destroy()
        except:
            errorBox.ErrorMessage(69)
    
    def dencrypt(self):
        try:
            for i in self.master.winfo_children():
                i.destroy()
        except:
            errorBox.ErrorMessage(69)


if __name__ == '__main__':
    app = app()
    app.mainloop()