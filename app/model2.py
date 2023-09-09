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
        # basic window configuration
        self.title("Translator")
        self.geometry("900x600")
        self.iconbitmap("images/translator_icon.ico")
        self.maxsize(width=900, height=600)    
        
        # background image
        self.background_image = Image.open("images/background04.jpg").resize((900,600))
        self.background = ImageTk.PhotoImage(self.background_image)
        
        # adding background to the window
        self.background_label = Label(self, image=self.background)
        self.background_label.place(relwidth=1, relheight=1)  
                
        # translator frame
        self.translator_frame = TranslatorFrame(self)
        #self.right_frame.pack(side="left", fill="y")
        
        self.welcome_frame = WelcomeFrame(self)
        self.welcome_frame.place(x=450, y=50) 
        
    def create_translator_frame(self):
        self.translator_frame.pack(side="left", fill="y")
    
    def destroy_welcome_frame(self):
        self.welcome_frame.destroy()
    
    def translator_page(self):
        self.create_translator_frame()
        self.destroy_welcome_frame()
        
    def speak(self):
        print("Testing speak button")
        
    def close_translator_frame(self):
        # close translator frame
        self.translator_frame.destroy()
        
        # open welcome frame
        self.welcome_frame
        self.welcome_frame.place(x=450, y=50) 

    def translate_it(self):
        # delete any previous translations
        self.translator_frame.translated_textbox.delete(1.0, END)
        try:
            # get languages from dictionary keys
            # get the from language key
            for key, value in self.translator_frame.languages.items():
                if (value == self.translator_frame.original_language_combo.get()):
                    from_language_key = key

            # get the to language key
            for key, value in self.translator_frame.languages.items():
                if (value == self.translator_frame.translated_language_combo.get()):
                    to_language_key = key
                
            # turn original text into a textblob 
            words = textblob.TextBlob(self.translator_frame.from_language_textbox.get(1.0, END))

            # translate text
            words = words.translate(
                from_lang=from_language_key,
                to = to_language_key)

            # output translated text to screen
            self.translator_frame.translated_textbox.insert(1.0, words)
        
            # initialize the speech engine
            #engine = pyttsx3.init()

            # pass text to speech engine
            #engine.say(words)

            # run to the engine
            #engine.runAndWait()

        except Exception as e:
            messagebox.showerror("Translator", e)
            
    def read_text(self, text_to_speech):
        text_to_speech = textblob.TextBlob(self.translator_frame.from_language_textbox.get(1.0, END))
        
        # initialize the speech engine
        engine = pyttsx3.init()
        
        # pass text to speech engine
        engine.say(text_to_speech)
        
        # run to the engine
        engine.runAndWait()
        
    def clear_textbox1(self):
        # clear the text boxes
        self.translator_frame.from_language_textbox.delete(1.0, END)
        
    def clear_textbox2(self):
        # clear the text boxes
        self.translator_frame.translated_textbox.delete(1.0, END)
        
class TranslatorFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # configuring the style of the frame 
        #self.width = 900
        #self.height = 850
        self.configure(fg_color="#5b3985")
        self.configure(width=450, height=1000)
        
        # Text font
        self.font_options = ("Georgia", 10)
        
        # configure grid system
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)  
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_columnconfigure(2, weight=3)
        #self.grid_columnconfigure(1, weight=1)
        #self.grid_columnconfigure(2, weight=2)
        
        # --------------variables------------------
        # Grab language list from GoogleTrans
        self.languages = googletrans.LANGUAGES

        # Convert to list
        self.language_list = list(self.languages.values())      
        
        # create widgets
        self.create_widgets()
        
    def create_widgets(self):
        
        # Row 0
        self.title_label = CTkLabel(self, text="Translator App")
        self.title_label.grid(row=0, column=0, columnspan=3, sticky="w", padx=10)
        
        self.corner_button = CTkButton(
            self, 
            text="x", 
            width=10, 
            command=self.master.close_translator_frame)
        self.corner_button.grid(row=0, column=3, sticky="ne")
        
        # Row 1
        self.original_language_combo = CTkComboBox(
            self, 
            width=100,
            button_hover_color="#46189f", 
            border_color="#6f38de",
            button_color="#6f38de",
            text_color="white",
            dropdown_fg_color="#6f38de",
            dropdown_hover_color="#46189f",
            values=self.language_list)
        self.original_language_combo.set("")
        self.original_language_combo.grid(row=1, column=0, sticky="sw", padx=10, pady=10)
        
        self.speak_from = CTkButton(
            self,
            text="speak", 
            font=("Impact", 10), 
            fg_color="#6f38de",
            hover_color="#46189f",
            text_color="white",            
            command=self.master.speak,
            width=10)
        self.speak_from.grid(row=1, column=0, padx=10, pady=10, sticky="se")

        self.clear_button1 = CTkButton(
            self,
            width=50,
            text="Clear", 
            font=("Impact", 20), 
            fg_color="#6f38de",
            hover_color="#46189f",
            text_color="white",            
            command=self.master.clear_textbox1)
        self.clear_button1.grid(row=1, column=2, sticky="sw", pady=10, padx=10)
        
        # Row 2
        self.from_language_textbox = CTkTextbox(self, width=40, height=100, fg_color="violet")
        self.from_language_textbox.grid(row=2, column=0, pady=10, padx=10, columnspan=3, sticky="news")
        self.from_language_textbox.configure(font=self.font_options)

        # Row 3  
        self.translate_button = CTkButton(
            self, 
            text="Translate", 
            font=("Impact", 20), 
            fg_color="#6f38de",         
            hover_color="#46189f",
            text_color="white",
            command=self.master.translate_it)
        self.translate_button.grid(row=3, column=0, padx=10, pady=10)    
        
        # Row 4
        self.translated_textbox = CTkTextbox(self, width=40, height=100)
        self.translated_textbox.grid(row=4, column=0, padx=10, pady=10, columnspan=3, sticky="nswe")
        self.translated_textbox.configure(font=self.font_options)
        
        # Row 5
        self.translated_language_combo = CTkComboBox(
            self, 
            width=100,
            button_hover_color="#46189f", 
            border_color="#6f38de",
            button_color="#6f38de",    
            text_color="white",  
            dropdown_fg_color="#6f38de",  
            dropdown_hover_color="#46189f",     
            values=self.language_list)
        self.translated_language_combo.set("")
        self.translated_language_combo.grid(row=5, column=0, padx=10, sticky="nw", pady=10)
        
        self.speak_to = CTkButton(
            self,
            text="speak", 
            font=("Impact", 10), 
            fg_color="#6f38de",
            hover_color="#46189f",
            text_color="white",            
            command=self.master.speak,
            width=10)
        self.speak_to.grid(row=5, column=0, sticky="ne", padx=10, pady=10) 
        
        self.clear_button2 = CTkButton(
            self,
            width=50,
            text="Clear", 
            font=("Impact", 20), 
            fg_color="#6f38de",
            hover_color="#46189f",
            text_color="white",            
            command=self.master.clear_textbox2)
        self.clear_button2.grid(row=5, column=2, sticky="nw", pady=10, padx=10)
        
class WelcomeFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.configure(width=80, height=60)
        self.configure(fg_color="#4c53be")
        
        # create widgets
        self.create_widgets()
        
    def create_widgets(self):
        # widgets
        
        self.welcome_label = CTkLabel(self, text="TRANSLATOR APP")
        self.welcome_label.pack(pady=10)
        
        self.welcome_btn = CTkButton(
            self, 
            text="Start",
            corner_radius=5,
            fg_color = "#4c53be",
            command=self.master.translator_page)
        self.welcome_btn.pack(pady=20)
                
# Running the application        
if __name__ == "__main__":
    app = App()
    app.mainloop()
    