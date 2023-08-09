from customtkinter import CTk, CTkFrame, CTkButton, CTkEntry,CTkComboBox
from tkinter import messagebox
from tkinter import ttk
import googletrans
import textblob
import pyttsx3

class App(CTk):
    def __init__(self):
        super().__init__()
        
        # basic configuration
        self.title("Translator")
        self.geometry("880x300")
        
        # main frame
        self.main_frame = MainFrame(self)


class MainFrame(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(expand = True, fill = "both")
        
        self.grid_rowconfigure((0, 1, 2), weight=1)  # configure grid system
        self.grid_columnconfigure((0, 1, 2), weight=1)

        # create the widgets
        self.create_widgets()
        
    def create_widgets(self):
        
        return None
        
        
        
if __name__ == "__main__":
    app = App()
    app.mainloop()