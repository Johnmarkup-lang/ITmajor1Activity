import sqlite3

connection = sqlite3.connect("da_answers.db")
cursor = connection.cursor()

command = """CREATE TABLE IF NOT EXISTS answer(id INTEGER PRIMARY KEY, answer TEXT)"""

cursor.execute("INSERT INTO answer VALUES ('true')")

connection.commit()