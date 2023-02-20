import sqlite3
import os

def create(name):
    con = sqlite3.connect(name)

def load(db):
    name, ext = os.path.splitext(db)
    if ext != ".langdb":
        return 1
    return 0
