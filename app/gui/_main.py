import customtkinter as ctk

class Main:
    def __init__(self, master):
        self.base = ctk.CTkFrame(master=master, fg_color="transparent")
        # Setup top level frame with single row and column
        self.base.grid(row=0, column=1, sticky="nsew")
        self.base.grid_rowconfigure(0, weight=1)
        self.base.grid_columnconfigure(0, weight=1)
        # Create default home frame
        self.home_frame = ctk.CTkFrame(master=self.base, fg_color="transparent")
        self.home_frame.grid_rowconfigure(0, weight=1)
        self.home_frame.grid_rowconfigure(1, weight=1)
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame.grid_columnconfigure(1, weight=1)
        self.home_frame.grid_columnconfigure(2, weight=1)
        welcome = ctk.CTkLabel(master=self.home_frame, text="Welcome", font=ctk.CTkFont(size=40, weight="bold"))
        welcome.grid(row=0, column=0, columnspan=3)
        button_padx, button_pady = 10, 5
        new = ctk.CTkButton(master=self.home_frame, text="New Database")
        new.grid(row=1, column=0, padx=button_padx, pady=button_pady, sticky="ew")
        load = ctk.CTkButton(master=self.home_frame, text="Load Database")
        load.grid(row=1, column=1, padx=button_padx, pady=button_pady, sticky="ew")
        merge = ctk.CTkButton(master=self.home_frame, text="Merge Databases")
        merge.grid(row=1, column=2, padx=button_padx, pady=button_pady, sticky="ew")
        # Show default home frame on startup
        self.frame = self.home_frame
        self.frame.grid(row=0, column=0, sticky="nsew")

    def show(self, frame):
        self.frame.grid_forget()
        self.frame = frame
        self.frame.grid(row=0, column=0, sticky="nsew")

