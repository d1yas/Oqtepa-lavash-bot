from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


pitsa_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Assorti 35 sm", callback_data="assorti_35sm_call"),
            InlineKeyboardButton("Pepperoni 35 sm", callback_data="pepperoni_35sm_call")
        ],
        [
            InlineKeyboardButton("Goshtli 35 sm", callback_data="goshtli_35sm_call"),
            InlineKeyboardButton("Qizil 45 sm", callback_data="qizil_45sm_call")
        ],
        [
            InlineKeyboardButton("Tovuqli 35 sm", callback_data="tovuqli_35sm_call")
        ],
        [
            InlineKeyboardButton("🔙 Orqaga", callback_data="orqaga_call")
        ]
    ], resize_keyboard=True
)