from tkinter import *
import googletrans
import textblob
from tkinter import ttk, messagebox
import pyttsx3

# Windows basic configuration
root = Tk()
root.title("Python Translator")
# root.iconbitmap("c:/gui/codemy.ico")
root.geometry("880x300")

# Functions
def translate_it():
    # delete any previous translations
    translated_text.delete(1.0, END)
    try:
        # get languages from dictionary keys
        # get the from language key
        for key, value in languages.items():
            if (value == original_combo.get()):
                from_language_key = key

        # get the to language key
        for key, value in languages.items():
            if (value == translated_combo.get()):
                to_language_key = key
                
        # turn original text into a textblob 
        words = textblob.TextBlob(original_text.get(1.0, END))

        # translate text
        words = words.translate(
            from_lang=from_language_key,
            to = to_language_key)

        # output translated text to screen
        translated_text.insert(1.0, words)

        # initialize the speech engine
        engine = pyttsx3.init()

        # pass text to speech engine
        engine.say(words)

        # run to the engine
        engine.runAndWait()

    except Exception as e:
        messagebox.showerror("Translator", e)

def clear():
    # clear the text boxes
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)

# Grab language list from GoogleTrans
languages = googletrans.LANGUAGES

# Convert to list
language_list = list(languages.values())


# Text Boxes
original_text = Text(root, height=10, width=40)
original_text.grid(row=0, column=0, pady=20, padx=10)

translate_button = Button(root, text="Translate!", font=("Helvetica", 24), command=translate_it)
translate_button.grid(row=0, column=1, padx=10)

translated_text = Text(root, height=10, width=40)
translated_text.grid(row=0, column=2, pady=20, padx=10)

# Combo boxes
original_combo = ttk.Combobox(root, width=50, value=language_list)
original_combo.current(21)
original_combo.grid(row=1, column=0)

translated_combo = ttk.Combobox(root, width=50, value=language_list)
translated_combo.current(21)
translated_combo.grid(row=1, column=2)

# Clear button
clear_button = Button(root, text="Clear", command=clear)
clear_button.grid(row=2, column=1)

# Run the program
root.mainloop()