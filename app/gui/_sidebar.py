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

    def __init__(self, main, sidebar, frame, text, command):
        Button._count += 1
        self._main = main
        self._frame = frame
        self._button = ctk.CTkButton(sidebar, text=text, command=command)
        self._button.grid(row=Button._count, column=0, padx=20, pady=10)
        
    def _command(self):
        self._main.show(self._frame)


class Home(Button):
    def __init__(self, main, sidebar):
        super().__init__(main, sidebar, main.home_frame, "Home", self._command)


class FindMatch(Button):
    def __init__(self, main, sidebar):
        super().__init__(main, sidebar, main.find_match_frame, "Find Matches", self._command)


class FindTranslation(Button):
    def __init__(self, main, sidebar):
        super().__init__(main, sidebar, main.find_translation_frame, "Find Translations", self._command)


class Update(Button):
    def __init__(self, main, sidebar):
        super().__init__(main, sidebar, main.update_frame, "Update Database", self._command)

