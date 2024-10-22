from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

lavashlar_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Original katta lavash", callback_data="Original_katta_lavash"),
            InlineKeyboardButton("Original kichik lavash", callback_data="Original_kichik_lavash")
        ],
        [
            InlineKeyboardButton("🧀 Pishloqli katta lavash", callback_data="Pishloqli_katta_lavash"),
            InlineKeyboardButton("🧀 Pishloqli kichik lavash", callback_data="Pishloqli_kichik_lavash")
        ],
        [
            InlineKeyboardButton("Tandir lavash", callback_data="Tandir_lavash"),
            InlineKeyboardButton("🧀 Pishloqli tandir lavash", callback_data="Pishloqli_tandir_lavash")
        ],
        [
            InlineKeyboardButton("🔙 Orqaga", callback_data="orqaga_call")
        ]
    ], resize_keyboard=True
)