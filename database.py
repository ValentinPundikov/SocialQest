import sqlite3
import os

def create_database():

    if not os.path.exists("data.db"):

        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()


        cursor.execute('''CREATE TABLE quests (
                            familia TEXT,
                            name TEXT,
                            surname TEXT,
                            quest TEXT,
                            date TEXT
                          )''')


        conn.commit()
        conn.close()

        print("База данных успешно создана.")
    else:
        print("Файл базы данных уже существует.")

def create_quest(typeq,fam,name,surname,date):
    try:
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO quests (familia, name, surname, quest, date) VALUES (?, ?, ?, ?, ?)", (fam, name, surname, typeq, date))
        conn.commit()
    except sqlite3.Error as e:
        print("Ошибка при выполнении SQL-запроса:", e)

def delete_quest(fam):
    try:
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM quests WHERE familia = ?", (fam,))
        conn.commit()
    except sqlite3.Error as e:
        print("Ошибка при выполнении SQL-запроса:", e)

def get_familia():
    try:
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT familia FROM quests")
        familia_data = cursor.fetchall()
        conn.close()
        return [row[0] for row in familia_data]
    except sqlite3.Error as e:
        print("Ошибка при выполнении SQL-запроса:", e)

def get_quests():
    try:
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT FROM quests")
        familia_data = cursor.fetchall()
        conn.close()
    except sqlite3.Error as e:
        print("Ошибка при выполнении SQL-запроса:", e)