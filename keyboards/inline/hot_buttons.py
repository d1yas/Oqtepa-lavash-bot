from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

qaynoq_ichimliklar_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Qora choy", callback_data="qora_choy_call"),
            InlineKeyboardButton("Ko'k choy", callback_data="kok_choy_call")
        ],
        [
            InlineKeyboardButton("🍋 Limonli Qora Choy", callback_data="limonli_qora_choy"),
            InlineKeyboardButton("🍋 Limonli Ko'k choy", callback_data="limonli_kok_choy")
        ],
        [
            InlineKeyboardButton("Kapuchino 300ml", callback_data="kapuchino_300_call"),
            InlineKeyboardButton("Latte 300 ml", callback_data="latte_300_call")
        ],
        [
            InlineKeyboardButton("Kapuchino 200 ml", callback_data="kapuchino_200_call"),
            InlineKeyboardButton("Americano 200 ml", callback_data="americano_200_call")
        ],
        [
            InlineKeyboardButton("Dabl espresso 200 ml", callback_data="dabl_espresso_200_call"),
            InlineKeyboardButton("Latte 400 ml", callback_data="latte_400_call")
        ],
        [
            InlineKeyboardButton("Americano 300 ml", callback_data="americano_300_call"),
            InlineKeyboardButton("Kapuchino 400 ml", callback_data="kapuchino_400_call")
        ],
        [
            InlineKeyboardButton("Latte 200 ml", callback_data="latte_200_call"),
            InlineKeyboardButton("Americano 400 ml", callback_data="americano_400_call")
        ],
        [
            InlineKeyboardButton("🔙 Orqaga", callback_data="orqaga_call")
        ]
    ], resize_keyboard=True
)

