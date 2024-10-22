from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


salatlar_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Mujskoy kapriz", callback_data="mujskoy_kapriz_call"),
            InlineKeyboardButton("Sezar", callback_data="sezar_call")
        ],
        [
            InlineKeyboardButton("🔙 Orqaga", callback_data="orqaga_call")
        ]
    ], resize_keyboard=True
)
