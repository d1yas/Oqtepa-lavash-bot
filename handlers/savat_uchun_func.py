from aiogram import types
from loader import dp
from keyboards.inline import savat_buttons
from keyboards.inline import category_buttons
# Initialize count as a global variable
count = 1

@dp.callback_query_handler(text=["plus_count_call", "minus_count_call"])
async def update_count(callback_query: types.CallbackQuery):
    global count

    # Adjust count based on button press
    if callback_query.data == "plus_count_call":
        count += 1
    elif callback_query.data == "minus_count_call" and count > 0:
        count -= 1

    # Directly update button text with the current count
    savat_buttons.savat.inline_keyboard[0][1].text = str(count)

    # Update the message’s keyboard to show the new count
    await callback_query.message.edit_reply_markup(reply_markup=savat_buttons.savat)