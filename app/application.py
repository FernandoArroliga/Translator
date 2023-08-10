from customtkinter import CTk, CTkFrame, CTkButton, CTkEntry,CTkComboBox
from tkinter import messagebox, END
from tkinter import ttk, Text
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
        
    def translate_it(self):
        # delete any previous translations
        self.main_frame.translated_text.delete(1.0, END)
        try:
            # get languages from dictionary keys
            # get the from language key
            for key, value in self.main_frame.languages.items():
                if (value == self.main_frame.original_combo.get()):
                    from_language_key = key

            # get the to language key
            for key, value in self.main_frame.languages.items():
                if (value == self.main_frame.translated_combo.get()):
                    to_language_key = key
                
            # turn original text into a textblob 
            words = textblob.TextBlob(self.main_frame.original_text.get(1.0, END))

            # translate text
            words = words.translate(
                from_lang=from_language_key,
                to = to_language_key)

            # output translated text to screen
            self.main_frame.translated_text.insert(1.0, words)

        except Exception as e:
            messagebox.showerror("Translator", e)
        
    def clear(self):
        # clear the text boxes
        self.main_frame.original_text.delete(1.0, END)
        self.main_frame.translated_text.delete(1.0, END)


class MainFrame(CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(expand = True, fill = "both")
        
        # configure grid system
        self.grid_rowconfigure((0, 1, 2), weight=1)  
        self.grid_columnconfigure((0, 1, 2), weight=1)
        
        # --------------variables------------------
        # Grab language list from GoogleTrans
        self.languages = googletrans.LANGUAGES

        # Convert to list
        self.language_list = list(self.languages.values())        

        # create the widgets
        self.create_widgets()
        
    def create_widgets(self):    
        # text boxes
        self.original_text = Text(self, height=10, width=40)
        self.original_text.grid(row=0, column=0, pady=20, padx=10)
        
        self.translate_button = CTkButton(
            self, 
            text="Translate!", 
            font=("Helvetica", 24), 
            command=self.master.translate_it)
        self.translate_button.grid(row=0, column=1, padx=10)
        
        self.translated_text = Text(self, height=10, width=40)
        self.translated_text.grid(row=0, column=2, pady=20, padx=10)
        
        # combo boxes
        self.original_combo = CTkComboBox(self, width=100, values=self.language_list)
        self.original_combo.set("")
        self.original_combo.grid(row=1, column=0)

        self.translated_combo = CTkComboBox(self, width=100, values=self.language_list)
        self.translated_combo.set("")
        self.translated_combo.grid(row=1, column=2)
                                         
        # clear button
        self.clear_button = CTkButton(self, text="Clear", command=self.master.clear)
        self.clear_button.grid(row=2, column=1)

# Running the application        
if __name__ == "__main__":
    app = App()
    app.mainloop()