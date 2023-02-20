import os
import customtkinter as ctk
import tkinter.filedialog as fd

from backend import create, load

class Main:
    def __init__(self, master):
        self._base = ctk.CTkFrame(master=master, fg_color="transparent")
        # Setup base frame with single row and column
        self._base.grid(row=0, column=1, sticky="nsew")
        self._base.grid_rowconfigure(0, weight=1)
        self._base.grid_columnconfigure(0, weight=1)
        # Create frames on top of the base frame
        self._create_home_frame()
        self._create_find_match_frame()
        self._create_find_translation_frame()
        self._create_update_frame()
        # Show default home frame on startup
        self._frame = self.home_frame
        self._frame.grid(row=0, column=0, sticky="nsew")

    def show(self, frame):
        self._frame.grid_forget()
        self._frame = frame
        self._frame.grid(row=0, column=0, sticky="nsew")

    def create(self):
        directory = fd.askdirectory(title="Choose Save Location")
        if not directory:
            return
        os.chdir(directory)
        name = ctk.CTkInputDialog(
            title="Database Name", text="Choose database name")
        name = name.get_input()
        if name:
            create(name + ".langdb")

    def load(self):
        db = fd.askopenfilename()
        if not db:
            return
        return_code = load(db)
        if return_code == 1:
            self._open_window_invalid_file()

    def _create_home_frame(self):
        self.home_frame = ctk.CTkFrame(
            master=self._base, fg_color="transparent")
        self.home_frame.grid_rowconfigure(0, weight=1)
        self.home_frame.grid_rowconfigure(1, weight=1)
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame.grid_columnconfigure(1, weight=1)
        self.home_frame.grid_columnconfigure(2, weight=1)
        welcome = ctk.CTkLabel(
            master=self.home_frame,
            text="Welcome",
            font=ctk.CTkFont(size=40, weight="bold")
        )
        welcome.grid(row=0, column=0, columnspan=3)
        button_padx, button_pady = 10, 5
        new = ctk.CTkButton(
            master=self.home_frame, text="New Database", command=self.create)
        new.grid(
            row=1, column=0, padx=button_padx, pady=button_pady, sticky="ew")
        load = ctk.CTkButton(
            master=self.home_frame, text="Load Database", command=self.load)
        load.grid(
            row=1, column=1, padx=button_padx, pady=button_pady, sticky="ew")
        merge = ctk.CTkButton(master=self.home_frame, text="Merge Databases")
        merge.grid(
            row=1, column=2, padx=button_padx, pady=button_pady, sticky="ew")

    def _create_find_match_frame(self):
        self.find_match_frame = ctk.CTkFrame(
            master=self._base, fg_color="transparent")
        self.find_match_frame.grid_columnconfigure(0, weight=1)
        self.find_match_frame.grid_rowconfigure(0, weight=1)
        self.find_match_frame.grid_rowconfigure(3, weight=4)
        title = ctk.CTkLabel(
            self.find_match_frame,
            text="Search Words",
            font=ctk.CTkFont(size=30, weight="bold")
        )
        title.grid(row=0, column=0, pady=(20, 10))
        word_entry = ctk.CTkEntry(
            self.find_match_frame, placeholder_text="word")
        word_entry.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        language_entry = ctk.CTkEntry(
            self.find_match_frame, placeholder_text="language")
        language_entry.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
        results_box = ctk.CTkTextbox(self.find_match_frame, state="disabled")
        results_box.grid(
            row=3, column=0, padx=20, pady=(10, 20), sticky="nsew")

    def _create_find_translation_frame(self):
        self.find_translation_frame = ctk.CTkFrame(
            master=self._base, fg_color="transparent")

    def _create_update_frame(self):
        self.update_frame = ctk.CTkFrame(
            master=self._base, fg_color="transparent")

    def _open_window_invalid_file(self):
        window = ctk.CTkToplevel()
        window.title("Error Loading File")
        window.geometry("300x100")
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)
        window.label = ctk.CTkLabel(
            window,
            text="Invalid file format. Expected .langdb file."
        )
        window.label.grid(row=0, column=0, sticky="nsew")
