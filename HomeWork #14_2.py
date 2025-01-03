# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Домашнее задание по теме "Выбор элементов и функции в SQL запросах"

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

#   1.Удалите из базы данных not_telegram.db запись с id = 6
cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

#   2.Подсчитать общее количество записей
cursor.execute('SELECT COUNT(*) FROM Users')
users_lot = cursor.fetchone()[0]

#   3.Посчитать сумму всех балансов
cursor.execute('SELECT SUM(balance) FROM Users')
balance_total = cursor.fetchone()[0]

#   4.Вывести в консоль средний баланс всех пользователей
cursor.execute('SELECT AVG(balance) FROM Users')
balance_average = cursor.fetchone()[0]
print('Средний баланс пользователей составляет -', balance_average)

connection.commit()
connection.close()





