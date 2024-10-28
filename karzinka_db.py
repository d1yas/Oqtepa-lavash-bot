# import sqlite3

# # Подключаемся к базе данных SQLite3 (или создаем её)
# conn = sqlite3.connect('cart.db')
# cursor = conn.cursor()

# # Создаем таблицу корзины, если она не существует
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS cart (
#     user_id INTEGER,
#     item_id INTEGER,
#     item_name TEXT,
#     quantity INTEGER,
#     PRIMARY KEY (user_id, item_id)
# )
# ''')

# conn.commit()


# def add_to_cart(user_id, item_id, item_name, quantity):
#     # Проверяем, есть ли товар уже в корзине
#     cursor.execute('SELECT quantity FROM cart WHERE user_id = ? AND item_id = ?', (user_id, item_id))
#     result = cursor.fetchone()

#     if result:
#         # Если товар уже есть, обновляем количество
#         new_quantity = result[0] + quantity
#         cursor.execute('UPDATE cart SET quantity = ? WHERE user_id = ? AND item_id = ?', (new_quantity, user_id, item_id))
#     else:
#         # Если товара нет, добавляем его в корзину
#         cursor.execute('INSERT INTO cart (user_id, item_id, item_name, quantity) VALUES (?, ?, ?, ?)', (user_id, item_id, item_name, quantity))


#     conn.commit()

# def show_cart(user_id):
#     cursor.execute('SELECT item_name, quantity FROM cart WHERE user_id = ?', (user_id,))
#     items = cursor.fetchall()

#     print("Корзина пользователя:")
#     for item_name, quantity in items:
#         print(f"{item_name}: {quantity} шт.")



# # Добавляем товар в корзину
# add_to_cart(user_id=1, item_id=101, item_name="Кетчуп", quantity=2)

# # Отображаем содержимое корзины
# show_cart(user_id=1)
