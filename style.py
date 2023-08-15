from customtkinter import CTk, CTkFrame, CTkButton, CTkEntry,CTkComboBox, set_default_color_theme, set_appearance_mode
from tkinter import messagebox, END
from tkinter import ttk, Text
import googletrans

set_default_color_theme("green")
set_appearance_mode("dark")

class App(CTk):
    def __init__(self):
        super().__init__()
        
        # basic configuration
        self.title("Translator")
        self.geometry("470x600")      
        
        # main frame
        self.main_frame = MainFrame(self)
        
    def translate_it(self):
        print("Testing app")
        
    def clear(self):
        # clear the text boxes
        self.main_frame.original_text.delete(1.0, END)
        self.main_frame.translated_text.delete(1.0, END)
    

class MainFrame(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(expand = True, fill = "both")
        
        # configure grid system
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)  
        self.grid_columnconfigure((0, 1, 2), weight=1)
        
        # --------------variables------------------
        # Grab language list from GoogleTrans
        self.languages = googletrans.LANGUAGES

        # Convert to list
        self.language_list = list(self.languages.values())        

        # create the widgets
        self.create_widgets()
        
    def create_widgets(self):
        self.original_combo = CTkComboBox(
            self, 
            width=100,
            button_hover_color="#99ffff", 
            border_color="#99ffff",
            button_color="#99ffff",
            text_color="black",
            values=self.language_list)
        self.original_combo.set("")
        self.original_combo.grid(row=0, column=0, sticky="sw", padx=20)
        
        self.original_text = Text(self, height=10, width=40)
        self.original_text.grid(row=1, column=0, pady=20, padx=20, columnspan=3, sticky="news")
       
        self.clear_button = CTkButton(
            self, 
            text="Clear", 
            font=("Helvetica", 20), 
            fg_color="#99ffff",
            hover_color="#dcffd7",
            text_color="black",            
            command=self.master.clear)
        self.clear_button.grid(row=0, column=2, sticky="sw")
       
        self.translated_text = Text(self, height=10, width=40)
        self.translated_text.grid(row=2, column=0, pady=10, padx=20, columnspan=3, sticky="news")
        
        self.translated_combo = CTkComboBox(
            self, 
            width=100,
            button_hover_color="#99ffff", 
            border_color="#99ffff",
            button_color="#99ffff",    
            text_color="black",         
            values=self.language_list)
        self.translated_combo.set("")
        self.translated_combo.grid(row=3, column=0, padx=20, sticky="nw")
        
        self.translate_button = CTkButton(
            self, 
            text="Translate", 
            font=("Helvetica", 20), 
            fg_color="#99ffff",
            hover_color="#dcffd7",
            text_color="black",
            command=self.master.translate_it)
        self.translate_button.grid(row=0, column=1,sticky="sw")

# Running the application        
if __name__ == "__main__":
    app = App()
    app.mainloop()