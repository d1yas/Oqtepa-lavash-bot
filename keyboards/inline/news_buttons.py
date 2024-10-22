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
            InlineKeyboardButton("Pishloqli Yo...alar 3 dona", callback_data="Pishloqli 3 dona_call"),
            InlineKeyboardButton("Pishloqli Yo...alar 5 dona", callback_data="Pishloqli 5 dona_call")
        ],
        [
            InlineKeyboardButton("Pishloqli Yo...alar t8 dona", callback_data="Pishloqli t8 dona_call"),
            InlineKeyboardButton("Qirsillama h...alar 3 dona", callback_data="Qirsillama h3 dona_call")
        ],
        [
            InlineKeyboardButton("Qirsillama h...alar 5 dona", callback_data="Qirsillama h5 dona_call"),
            InlineKeyboardButton("Qirsillama h...alar 8 dona", callback_data="Qirsillama h8 dona_call")
        ],
        [
            InlineKeyboardButton("🔙 Orqaga", callback_data="orqaga_call")
        ]
    ], resize_keyboard=True
)
