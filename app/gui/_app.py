import customtkinter as ctk
from gui._main import Main
from gui._sidebar import Sidebar

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Conlang Toolkit")
        self.geometry("900x450+100+100")
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        main = Main(master=self)
        sidebar = Sidebar(master=self, main=main)

