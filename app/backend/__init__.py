import sqlite3
import os

def create_db(db):
    print(f"created {db}")
    con = sqlite3.connect(db)

def load_db(db):
    name, ext = os.path.splitext(db)
    if ext != ".langdb":
        print(f"failed to load {db}")
        return 1
    con = sqlite3.connect(db)
    print(f"loaded {db}")
    return 0
