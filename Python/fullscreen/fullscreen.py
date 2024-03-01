import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Full screen")        
        self.resizable(True, True) # width, height
        self.grid_rowconfigure(0, weight=1) # Strech grid 1st row horizontalyin in frame
        self.columnconfigure(0, weight=1) # Strech grid 1rd column verticaly in frame        
        self.toplevel_window = None

        label = customtkinter.CTkLabel(self, text="Presss Esc")
        label.pack()

    def update(self):
        print("Works...")
        self.after(10000, self.update)

    def fullscreen(self):
        # Fullscreen scaling (required before app class obj)
        # customtkinter.deactivate_automatic_dpi_awareness()
        # customtkinter.set_window_scaling(1)
        # Enable
        self.wm_attributes('-fullscreen', True)        
        self.bind("<Escape>", lambda x: self.destroy())

if __name__ == "__main__":
    # Theme
    # customtkinter.set_default_color_theme("themes/atomjoy.json")
    customtkinter.set_default_color_theme("blue")    
    
    # Mode
    customtkinter.set_appearance_mode("dark")
    # customtkinter.set_appearance_mode("light")

    # Required for fullscreen()
    customtkinter.deactivate_automatic_dpi_awareness()
    customtkinter.set_window_scaling(1)
    
    # Run    
    app = App()
    
    app.fullscreen()

    app.update()
    app.mainloop()