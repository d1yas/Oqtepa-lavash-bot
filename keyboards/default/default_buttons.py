from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

for_start = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🇺🇿 O'zbekcha")
        ],
        [
            KeyboardButton("🇷🇺 Русский")
        ],
        [
            KeyboardButton("🇺🇸 English")
        ]
    
    ],
    resize_keyboard=True
)

send_nomer = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("📞 Telefon raqamni yuborish", request_contact=True)
        ]
    ],
    resize_keyboard=True
)   

shaharlar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Toshkent"),
            KeyboardButton("Nukus")
        ],
        [
            KeyboardButton("Namangan"),
            KeyboardButton("Qoqon")
        ],
        [
            KeyboardButton("Andijon"),
            KeyboardButton("Farg'ona")
        ],
        [
           KeyboardButton("Samarqand"),
           KeyboardButton("Gazalkent")
        ],
        [
            KeyboardButton("Urgench")
        ]
    ],
    resize_keyboard=True
)

borib_buyurtma = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🛵 Eltib berish"),
            KeyboardButton("🚶‍♂️ Borib olish")
        ],
        [
            KeyboardButton("🔙 Ortga")
        ]
        
    ],
    resize_keyboard=True
)

borib_buyurtma_ortga = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("📍 Geo-joylashuvni yuborish",request_location=True)
        ],
        [
            KeyboardButton("🔙 Ortga")
        ]
    ],
    resize_keyboard=True
)



