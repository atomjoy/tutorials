from customtkinter import CTk, CTkToplevel, CTkLabel, CTkButton

class ToplevelWindow(CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.label = CTkLabel(self, text="This is a Toplevel Window")
        self.label.pack(padx=20, pady=20)


class App(CTk):
    def __init__(self):
        super().__init__()

        self.button = CTkButton(self, text="Open toplevel new window", command=self.open_toplevel)
        self.button.pack(padx=20, pady=20)

        self.toplevel_window = None

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed            
            self.toplevel_window.attributes('-topmost', True)
        else:
            self.toplevel_window.focus()  # if window exists focus it
            self.toplevel_window.attributes('-topmost', True)


if __name__ == "__main__":
    app = App()
    app.mainloop()