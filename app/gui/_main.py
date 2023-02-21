import os
import customtkinter as ctk
import tkinter.filedialog as fd

import gui._popups as popup
from backend import create_db, load_db

class Main:
    """
    The main display window.

    Public Attributes
    -----------------
    find_match_frame : ctk.CTkFrame
        Allows the user to search for words in the database that match
        their given input. Users can also restrict the search to
        specific languages. The result is shown in a large textbox.
    find_translation_frame : ctk.CTkFrame
        Allows the user to translate a word/phrase from one language
        to any selection of languages within the database.
    home_frame : ctk.CTkFrame
        The window displayed on start-up of the app. Allows the user
        to create, load, or merge databases.
    update_frame : ctk.CTkFrame
        Allows the user to update the database by adding new entries,
        or editing/deleting existing ones.

    Public Methods
    --------------
    show(frame)
        Remove the current frame (self._frame) from the main display
        and replace with the input frame

    Private Attributes
    ------------------
    _master : ctk.CTk
        The app window that holds all gui elements
    _base : ctk.CTkFrame
        The base frame upon which all other frames sit on.
    _frame : ctk.CTkFrame
        The currently displayed frame.

    Private Methods
    ---------------
    _app_pos(offx, offy)
        x- and y-position of the app window, plus some given offsets
    _create_db()
        Create a new language database
    _load_db()
        Load an existing language database
    """
    def __init__(self, master):
        self._master = master
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
        self._frame = self._home_frame
        self._frame.grid(row=0, column=0, sticky="nsew")

    def show(self, frame):
        if self._frame != frame:
            self._frame.grid_forget()
            self._frame = frame
            self._frame.grid(row=0, column=0, sticky="nsew")

    def _app_pos(self, offx=100, offy=100):
        return self._master.winfo_x() + offx, self._master.winfo_y() + offy

    def _create_db(self):
        directory = fd.askdirectory(title="Choose Save Location")
        if not directory:
            return
        os.chdir(directory)
        x, y = self._app_pos()
        name = ctk.CTkInputDialog(
            title="Database Name", text="Choose database name")
        name.geometry(f"400x150+{x}+{y}")
        name = name.get_input()
        if not name:
            return
        name += ".langdb"
        if os.path.exists(name):
            posx, posy = self._app_pos()
            popup.file_name_already_in_use(name, posx, posy)
        else:
            create_db(name)

    def _load_db(self):
        db = fd.askopenfilename()
        if not db:
            return
        return_code = load_db(db)
        if return_code == 1:
            posx, posy = self._app_pos()
            popup.invalid_file_type(posx, posy)

    #--------------------FRAME CREATION FUNCTIONS--------------------
    def _create_find_match_frame(self):
        self._find_match_frame = ctk.CTkFrame(
            master=self._base, fg_color="transparent")
        self._find_match_frame.grid_columnconfigure(0, weight=1)
        self._find_match_frame.grid_rowconfigure(0, weight=1)
        self._find_match_frame.grid_rowconfigure(3, weight=4)
        title = ctk.CTkLabel(
            self._find_match_frame,
            text="Search Words",
            font=ctk.CTkFont(size=30, weight="bold")
        )
        title.grid(row=0, column=0, pady=(20, 10))
        word_entry = ctk.CTkEntry(
            self._find_match_frame, placeholder_text="word")
        word_entry.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        language_entry = ctk.CTkEntry(
            self._find_match_frame, placeholder_text="language")
        language_entry.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
        results_box = ctk.CTkTextbox(self._find_match_frame, state="disabled")
        results_box.grid(
            row=3, column=0, padx=20, pady=(10, 20), sticky="nsew")

    def _create_find_translation_frame(self):
        self._find_translation_frame = ctk.CTkFrame(
            master=self._base, fg_color="transparent")

    def _create_home_frame(self):
        self._home_frame = ctk.CTkFrame(
            master=self._base, fg_color="transparent")
        self._home_frame.grid_rowconfigure(0, weight=1)
        self._home_frame.grid_rowconfigure(1, weight=1)
        self._home_frame.grid_columnconfigure(0, weight=1)
        self._home_frame.grid_columnconfigure(1, weight=1)
        self._home_frame.grid_columnconfigure(2, weight=1)
        welcome = ctk.CTkLabel(
            master=self._home_frame,
            text="Welcome",
            font=ctk.CTkFont(size=40, weight="bold")
        )
        welcome.grid(row=0, column=0, columnspan=3)
        button_padx, button_pady = 10, 5
        new = ctk.CTkButton(
            master=self._home_frame,
            text="New Database",
            command=self._create_db
        )
        new.grid(
            row=1, column=0, padx=button_padx, pady=button_pady, sticky="ew")
        load = ctk.CTkButton(
            master=self._home_frame,
            text="Load Database",
            command=self._load_db
        )
        load.grid(
            row=1, column=1, padx=button_padx, pady=button_pady, sticky="ew")
        merge = ctk.CTkButton(master=self._home_frame, text="Merge Databases")
        merge.grid(
            row=1, column=2, padx=button_padx, pady=button_pady, sticky="ew")

    def _create_update_frame(self):
        self._update_frame = ctk.CTkFrame(
            master=self._base, fg_color="transparent")

    #------------------------PUBLIC ATTRIBUTES------------------------
    @property
    def find_match_frame(self):
        return self._find_match_frame

    @property
    def find_translation_frame(self):
        return self._find_translation_frame

    @property
    def home_frame(self):
        return self._home_frame

    @property
    def update_frame(self):
        return self._update_frame

