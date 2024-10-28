from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

lavashlar_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Original katta lavash", callback_data="original_katta_lavash"),
            InlineKeyboardButton("Original kichik lavash", callback_data="original_kichik_lavash")
        ],
        [
            InlineKeyboardButton("🧀 Pishloqli katta lavash", callback_data="pishloqli_katta_lavash"),
            InlineKeyboardButton("🧀 Pishloqli kichik lavash", callback_data="pishloqli_kichik_lavash")
        ],
        [
            InlineKeyboardButton("Tandir lavash", callback_data="tandir_lavash"),
            InlineKeyboardButton("🧀 Pishloqli tandir lavash", callback_data="pishloqli_tandir_lavash")
        ],
        [
            InlineKeyboardButton("🔙 Orqaga", callback_data="orqaga_lavash_call")
        ]
    ], resize_keyboard=True
)

