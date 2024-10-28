from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

souslar_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Ketchup", callback_data="ketchup_call"),
            InlineKeyboardButton("Chili souse", callback_data="chili_souse_call")
        ],
        [
            InlineKeyboardButton("Pishloqli souse", callback_data="pishloqli_souse_call"),
            InlineKeyboardButton("Oq souse", callback_data="oq_souse_call")
        ],
        [
            InlineKeyboardButton("Souslar kvarteti", callback_data="souslar_kvarteti_call"),
            InlineKeyboardButton("Souslar dueti", callback_data="souslar_dueti_call")
        ],
        [
            InlineKeyboardButton("🔙 Orqaga", callback_data="orqaga_call")
        ]
    ], resize_keyboard=True
)