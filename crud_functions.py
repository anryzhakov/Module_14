import sqlite3

# Создаем таблицу Products в базе данных
def initiate_db():
    connection = sqlite3.connect('productsDB.db')
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Products(
                        id INTEGER PRIMARY KEY,
                        title TEXT NOT NULL,
                        description TEXT NOT NULL,
                        price INTEGER NOT NULL
                        )
                    ''')

    connection.commit()
    connection.close()

# Получение всего списка продуктов из базы
def get_all_products():
    connection = sqlite3.connect('productsDB.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()

    connection.close()
    return products

def add_product(title, description, price):
    connection = sqlite3.connect('productsDB.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                   (title, description, price))

    connection.commit()
    connection.close()