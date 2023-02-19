import customtkinter as ctk


class Sidebar:
    def __init__(self, master, main):
        # Sidebar
        sidebar = ctk.CTkFrame(master, width=140, corner_radius=0)
        sidebar.grid(row=0, column=0, sticky="nsew")
        # Sidebar Label
        self.logo_label = ctk.CTkLabel(sidebar, text="Options", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        # Sidebar Buttons
        Home(main, sidebar)
        FindMatch(main, sidebar)
        FindTranslation(main, sidebar)
        Update(main, sidebar)


class Button:
    _count = 0

    def __init__(self, main, sidebar, text, command):
        self._main = main
        self.frame = ctk.CTkFrame(master=main.base, fg_color="transparent")
        self.button = ctk.CTkButton(sidebar, text=text, command=command)
        Button._count += 1
        self.button.grid(row=Button._count, column=0, padx=20, pady=10)
        
    def _command(self):
        self._main.show(self.frame)


class Home(Button):
    def __init__(self, main, sidebar):
        super().__init__(main, sidebar, "Home", self._command)
        self.frame = self._main.home_frame


class FindMatch(Button):
    def __init__(self, main, sidebar):
        super().__init__(main, sidebar, "Find Matches", self._command)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(3, weight=4)
        title = ctk.CTkLabel(self.frame, text="Search Words", font=ctk.CTkFont(size=30, weight="bold"))
        title.grid(row=0, column=0, pady=(20, 10))
        word_entry = ctk.CTkEntry(self.frame, placeholder_text="word")
        word_entry.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        language_entry = ctk.CTkEntry(self.frame, placeholder_text="language")
        language_entry.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
        results_box = ctk.CTkTextbox(self.frame, state="disabled")
        results_box.grid(row=3, column=0, padx=20, pady=(10, 20), sticky="nsew")


class FindTranslation(Button):
    def __init__(self, main, sidebar):
        super().__init__(main, sidebar, "Find Translations", self._command)


class Update(Button):
    def __init__(self, main, sidebar):
        super().__init__(main, sidebar, "Update Database", self._command)

