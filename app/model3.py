from customtkinter import *

class App(CTk):
    def __init__(self):
        super().__init__()

        # Basic configuration
        self.title("Testing App")
        self.geometry("600x400")
        
        # Main Frame
        self.main_frame = MainFrame(self)
        self.main_frame.pack(pady=10)

        self.sub_frame = SubFrame(self)
                
    def updates(self):
        self.sub_frame.pack(pady=10, expand=True, fill="both")
    
        
    def destroy(self):
        self.main_frame.destroy()

class MainFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # Create widgets
        self.create_widgets()
        
    def create_widgets(self):
        self.label1 = CTkLabel(self, text="This is my text")
        self.label1.pack(pady=10)

        self.btn1 = CTkButton(self, text="Press me!", command=self.master.updates)
        self.btn1.pack(pady=10)

        self.btn2 = CTkButton(self, text="Destroy", command=self.master.destroy)
        self.btn2.pack(pady=10)       

class SubFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # basic configuration
        self.pack(pady=10)
        
        # create widgets
        self.create_widgets()
        
    def create_widgets(self):
        
        self.info = CTkLabel(self, text="Hello world")
        self.info.pack(expand=True, fill="both")

if __name__ == "__main__":
    app = App()
    app.mainloop()