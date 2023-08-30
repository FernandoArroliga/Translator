# Importing the useful libraries and modules
from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel, CTkEntry,CTkComboBox, set_default_color_theme, set_appearance_mode, CTkTextbox
from tkinter import messagebox, END
from tkinter import ttk, Text, Label
import googletrans
from PIL import Image, ImageTk
import textblob
import pyttsx3

# Setting the application theme
set_default_color_theme("dark-blue")
set_appearance_mode("dark")

class App(CTk):
    def __init__(self):
        super().__init__()
        #--------- Basic Window Configuration---------
        # basic window configuration
        self.title("Translator")
        self.geometry("900x600")
        self.iconbitmap("images/translator_icon.ico")
        self.maxsize(width=900, height=600)    
        
        # frame size
        #frame_width = 600
        #frame_height = 650  
        
        # background image
        self.background_image = Image.open("images/background01.jpg").resize((900,600))
        self.background = ImageTk.PhotoImage(self.background_image)
        
        # adding background to the window
        self.background_label = Label(self, image=self.background)
        self.background_label.place(relwidth=1, relheight=1)  
                
        # main frame
        self.right_frame = RightFrame(self)
        #self.right_frame.place(x=350, y=50)
        self.right_frame.pack()
    
    def translate_it(self):
        # delete any previous translations
        self.right_frame.translated_text.delete(1.0, END)
        try:
            # get languages from dictionary keys
            # get the from language key
            for key, value in self.right_frame.languages.items():
                if (value == self.right_frame.original_combo.get()):
                    from_language_key = key

            # get the to language key
            for key, value in self.right_frame.languages.items():
                if (value == self.right_frame.translated_combo.get()):
                    to_language_key = key
                
            # turn original text into a textblob 
            words = textblob.TextBlob(self.right_frame.original_text.get(1.0, END))

            # translate text
            words = words.translate(
                from_lang=from_language_key,
                to = to_language_key)

            # output translated text to screen
            self.right_frame.translated_text.insert(1.0, words)
        
            # initialize the speech engine
            #engine = pyttsx3.init()

            # pass text to speech engine
            #engine.say(words)

            # run to the engine
            #engine.runAndWait()

        except Exception as e:
            messagebox.showerror("Translator", e)
            
    def read_text(self, text_to_speech):
        text_to_speech = textblob.TextBlob(self.right_frame.original_text.get(1.0, END))

        
        # initialize the speech engine
        engine = pyttsx3.init()
        
        # pass text to speech engine
        engine.say(text_to_speech)
        
        # run to the engine
        engine.runAndWait()
        
    def clear(self):
        # clear the text boxes
        self.right_frame.original_text.delete(1.0, END)
        self.right_frame.translated_text.delete(1.0, END)
        
class RightFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # configuring the style of the frame 
        self.width = 900
        self.height = 850
        #self.configure(width=self.width, height=self.height)
        self.configure(fg_color="black")
        
        # Text font
        self.font_options = ("Georgia", 10)
        
        # configure grid system
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)  
        self.grid_columnconfigure((0, 1, 2), weight=1)
        
        # --------------variables------------------
        # Grab language list from GoogleTrans
        self.languages = googletrans.LANGUAGES

        # Convert to list
        self.language_list = list(self.languages.values())      
        
        # create widgets
        self.create_widgets()
        
    def create_widgets(self):
        
        # First row
        self.original_combo = CTkComboBox(
            self, 
            width=100,
            button_hover_color="#46189f", 
            border_color="#6f38de",
            button_color="#6f38de",
            text_color="white",
            dropdown_fg_color="#6f38de",
            dropdown_hover_color="#46189f",
            values=self.language_list)
        self.original_combo.set("")
        self.original_combo.grid(row=0, column=0, sticky="sw", padx=20, pady=10)
        
        self.speak_from = CTkButton(
            self,
            text= "speak")
        self.speak_from.grid(row=0, column=1)

        self.clear_button = CTkButton(
            self,
            text="Clear", 
            font=("Impact", 20), 
            fg_color="#6f38de",
            hover_color="#46189f",
            text_color="white",            
            command=self.master.clear)
        self.clear_button.grid(row=0, column=2, sticky="sw", padx=20, pady=10)
        

        # Second row
        #self.original_text = Text(self, height=10, width=40)
        #self.original_text.grid(row=1, column=0, pady=20, padx=20, columnspan=3, sticky="news")
        #self.original_text.configure(font=self.font_options)
        
        self.from_language_textbox = CTkTextbox(self, width=40, height=200, fg_color="violet")
        self.from_language_textbox.grid(row=1, column=0, pady=20, padx=20, columnspan=3, sticky="news")

    
        # Third row   
        #self.translated_text = Text(self, height=10, width=40)
        #self.translated_text.grid(row=2, column=0, pady=10, padx=20, columnspan=3, sticky="news")
        #self.translated_text.configure(font=self.font_options)
        self.translate_button = CTkButton(
            self, 
            text="Translate", 
            font=("Impact", 20), 
            fg_color="#6f38de",         
            hover_color="#46189f",
            text_color="white",
            command=self.master.translate_it)
        self.translate_button.grid(row=2, column=0,sticky="sw", padx=20, pady=10)            
        
        # fourth row
        self.translated_textbox = CTkTextbox(self, width=40, height=200)
        self.translated_textbox.grid(row=2, column=0, pady=20, padx=20, columnspan=3, sticky="news")
        self.translated_textbox.configure(font=self.font_options)
        
        self.translated_combo = CTkComboBox(
            self, 
            width=100,
            button_hover_color="#46189f", 
            border_color="#6f38de",
            button_color="#6f38de",    
            text_color="white",  
            dropdown_fg_color="#6f38de",  
            dropdown_hover_color="#46189f",     
            values=self.language_list)
        self.translated_combo.set("")
        self.translated_combo.grid(row=4, column=0, padx=20, sticky="nw", pady=10)

        self.speak_from = CTkButton(
            self,
            text= "speak")
        self.speak_from.grid(row=0, column=1)        
        
        
# Running the application        
if __name__ == "__main__":
    app = App()
    app.mainloop()