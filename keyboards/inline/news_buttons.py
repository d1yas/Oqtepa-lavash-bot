from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

yangiliklar_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Sezar vrap", callback_data="sezar_vrap_call"),
            InlineKeyboardButton("BBQ vrab", callback_data="bbq_vrap_call")
        ],
        [
            InlineKeyboardButton("Qisllimala hot dog", callback_data="qisllimala_hot_dog_call"),
            InlineKeyboardButton("Kenja hot dog", callback_data="kenja_hot_dog_call")
        ],
        [
            InlineKeyboardButton("Tovuqli looonger", callback_data="tovuqli_looonger_call"),
            InlineKeyboardButton("Qizil karamli salat", callback_data="qizil_karamli_salat_call")
        ],
        [
            InlineKeyboardButton("Vrap master", callback_data="vrap_master_call"),
            InlineKeyboardButton("Kanadalik fri", callback_data="kanadalik_fri_call")
        ],
        [
            InlineKeyboardButton("Pishloqli Yostiqchalar 3 dona", callback_data="pishloqli_3_call"),
            InlineKeyboardButton("Pishloqli Yostiqchalar 5 dona", callback_data="pishloqli_5_call")
        ],
        [
            InlineKeyboardButton("Pishloqli Yostiqchalar 8 dona", callback_data="pishloqli_8_call"),
            InlineKeyboardButton("Qirsillama  halchalar 3 dona", callback_data="qirsillama_3_call")
        ],
        [
            InlineKeyboardButton("Qirsillama halchalar 5 dona", callback_data="qirsillama_5_call"),
            InlineKeyboardButton("Qirsillama halchalar 8 dona", callback_data="qirsillama_8_call")
        ],
        [
            InlineKeyboardButton("🔙 Orqaga", callback_data="orqaga_news__call")
        ]
    ], resize_keyboard=True
)
