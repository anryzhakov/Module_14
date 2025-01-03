# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Домашнее задание по теме "Создание БД, добавление, выбор и удаление элементов."

import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

#for j in range(10):
#     cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
#                    (f'User{j+1}', f'example{j+1}@gmail.com', f'{(j+1)*10}', '1000'))
#   if (j % 2) == False:
#         cursor.execute('UPDATE Users SET balance = ? WHERE username = ?',
#                        (500, f'User{j+1}'))
#    if (j % 3) == False:
#        cursor.execute('DELETE FROM Users WHERE username = ?', (f'User{j+1}',))

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))
users = cursor.fetchall()
for user in users:
    print(user)

connection.commit()
connection.close()





