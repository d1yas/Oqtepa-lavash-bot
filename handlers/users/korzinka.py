from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db_file import *
from states.oqtepa_states import OqtepaState
from karzinka_db import *

import sqlite3

# Подключаемся к базе данных SQLite3 (или создаем её)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Создаем таблицу корзины, если она не существует
cursor.execute('''
CREATE TABLE IF NOT EXISTS savatcha (
    user_id INTEGER,
    item_id INTEGER,
    item_name TEXT,
    about_food TEXT,
    count INTEGER,
    price INTEGER,
    total_price INTEGER,
    PRIMARY KEY (user_id, item_id)
)
''')

conn.commit()

def add_savatcha(user_id, item_id, item_name, quantity, price, total_price):
    cursor.execute('INSERT INTO savatcha (user_id, item_id, item_name, about_food, count) VALUES (?, ?, ?, ?)', (user_id, item_id, item_name, quantity))
    conn.commit()

# @dp.callback_query_handler(text="savatga_qoshish_call")
# async def savatga_qoshish_func(call: types.CallbackQuery):
    