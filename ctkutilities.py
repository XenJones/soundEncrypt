import customtkinter


class MessageBox(customtkinter.CTkToplevel):
    def __init__(self, master, title, message_text, button_text):
        super().__init__()
        self.geometry('400x100')
        self.title(title)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        if message_text is not None:
            self.label = customtkinter.CTkLabel(self, text=message_text)
            self.label.grid(column=0, row=0, padx=10, pady=10)

        if button_text is not None:
            self.button = customtkinter.CTkButton(self, text=button_text, command=self.destroy)
            self.button.grid(column=0, row=1, padx=10, pady=10)

        self.transient(master)
        self.grab_set()