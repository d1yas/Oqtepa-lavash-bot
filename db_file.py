import sqlite3


connect = sqlite3.connect('db.sqlite3')
cursor = connect.cursor()

def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        phone_number TEXT,
        city TEXT,
        language TEXT
    )""")
    connect.commit()


def insert_data(phone_number, city, language):
    cursor.execute("INSERT INTO users (phone_number, city, language) VALUES (?, ?, ?)", (phone_number, city, language))
    connect.commit()

create_table()



# def select_data():
#     cursor.execute("SELECT * FROM users WHERE phone_number = ? AND city = ? AND language = ?", (telefon, shahar, til))
#     return cursor.fetchall()

# print(select_data())