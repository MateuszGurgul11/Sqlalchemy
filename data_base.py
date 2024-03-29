import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """Create connecting"""
    conn = None

    try:
        conn = sqlite3.connect(db_file)
        print(f"connected to {db_file}")
    except Error as e:
        print(e)

if __name__ == "__main__":
    db_file = "database.db"
    conn = create_connection(db_file)

