from view import View
import sqlite3
from sqlite3 import Error

def db_Connect(f_name):
    try:
        connect = sqlite3.connect(f_name)
        return connect
    except Error as e:
        print(e)



if __name__ == '__main__':
    crTable = db_Connect("crtable.db")
    c = View(crTable)