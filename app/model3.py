from customtkinter import *

"""
# Main configuration
window = CTk()
window.title("Testing App")
window.geometry("600x400")

# Functionality
def updates():
    label1.configure(text="Hello World")

def night_mode():
    set_default_color_theme("dark-blue")
    set_appearance_mode("dark")   

# Widgets
label1 = CTkLabel(window, text="This is my text")
label1.pack(pady=10)

btn1 = CTkButton(window, text="Press me!", command=updates)
btn1.pack(pady=10)

btn2 = CTkButton(window, text="c:", command=night_mode)
btn2.pack(pady=10)

# Run the application
window.mainloop()

"""

class App(CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Basic configuration
        self.title("Testing App")
        self.geometry("600x400")
        
        # Main Frame
        self.main_frame = MainFrame(self)

    def updates(self):
        print("Testing")
        
    def destroy(self):
        self.main_frame.destroy()

class MainFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # basic configuration
        self.pack(pady=10)
        
        # Create widgets
        self.create_widgets()
        
    def create_widgets(self):
        self.label1 = CTkLabel(self, text="This is my text")
        self.label1.pack(pady=10)

        self.btn1 = CTkButton(self, text="Press me!", command=self.master.updates)
        self.btn1.pack(pady=10)

        self.btn2 = CTkButton(self, text="Destroy", command=self.master.destroy)
        self.btn2.pack(pady=10)       
        

if __name__ == "__main__":
    app = App()
    app.mainloop()