import customtkinter as ctk

from backend import load_db


class _PopUp(ctk.CTkToplevel):
    def __init__(self, title, width, height, posx, posy):
        super().__init__()
        self.geometry(f"{width}x{height}+{posx}+{posy}")
        self.title(title)
        self.resizable(False, False)


def file_name_already_in_use(name, posx, posy):
    def yes_load():
        load_db(name)
        window.destroy()

    def no_load():
        window.label.destroy()
        window.yes_button.destroy()
        window.no_button.destroy()
        window.label = ctk.CTkLabel(
            master=window,
            text=(
                "Database creation cancelled. If you would like to make a "
                f"new database with the name {name}, move {name} to "
                f"another directory, delete {name}, or select a different "
                "directory."
            ),
            wraplength=360
        )
        window.label.grid(row=0, column=0, columnspan=2, sticky="nsew")
        window.ok_button = ctk.CTkButton(
            master=window, text="OK", command=window.destroy)
        window.ok_button.grid(
            row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    window = _PopUp("File Name Already In Use", 400, 150, posx, posy)
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.label = ctk.CTkLabel(
        master=window,
        text=(
            f"A file with the name {name} already exists in this directory. "
            "Would you like to load this database instead of creating "
            "a new one?"
        ),
        wraplength=360
    )
    window.label.grid(row=0, column=0, columnspan=2, sticky="nsew")
    window.yes_button = ctk.CTkButton(
        master=window, text="Yes", command=yes_load)
    window.yes_button.grid(row=1, column=0)
    window.no_button = ctk.CTkButton(
        master=window, text="No", command=no_load)
    window.no_button.grid(row=1, column=1)

def invalid_file_type(posx, posy):
    window = _PopUp("Error Loading File", 300, 100, posx, posy)
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.label = ctk.CTkLabel(
        window,
        text="Invalid file format. Expected .langdb file."
    )
    window.label.grid(row=0, column=0, sticky="nsew")
