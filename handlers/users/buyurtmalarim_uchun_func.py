# from aiogram import types
# from loader import dp
# from keyboards.inline.inline_buttons import get_order_keyboard

# user_orders = {}
# user_counts = {}


# @dp.callback_query_handler(text=["my_tovar"])
# async def show_cart(callback_query: types.CallbackQuery):
#     user_id = callback_query.from_user.id
#     orders = user_orders.get(user_id, [])
    
#     if orders:
#         orders_text = "\n".join(orders)
#         await callback_query.answer(f"🛍 Sizning buyurtmalaringiz:\n{orders_text}", show_alert=True)
#     else:
#         await callback_query.answer("🛍 Sizning buyurtmalaringiz bo'sh.", show_alert=True)


# @dp.callback_query_handler(text=["add_to_cart"])  # Adjust the callback name as needed
# async def add_to_cart(callback_query: types.CallbackQuery):
#     user_id = callback_query.from_user.id

#     # Initialize user's cart if not exists
#     if user_id not in user_orders:
#         user_orders[user_id] = []

#     # Example item to add
#     item_name = "Item"  # Replace this with the actual item name
#     current_count = user_counts.get(user_id, 1)
    
#     # Create a unique identifier for the item in the cart
#     order_item = f"{item_name} x{current_count}"
    
#     # Add selected item with current count to cart
#     user_orders[user_id].append(order_item)

#     await callback_query.answer(f"{item_name} savatga qo'shildi!", show_alert=True)


# # Command to show orders
# @dp.message_handler(commands=["orders"])
# async def show_orders(message: types.Message):
#     user_id = message.from_user.id
#     orders = user_orders.get(user_id, [])
    
#     if orders:
#         orders_text = "\n".join(orders)
#         await message.answer(f"🛍 Sizning buyurtmalaringiz:\n{orders_text}")
#     else:
#         await message.answer("🛍 Sizning buyurtmalaringiz bo'sh.")


# # Optional: Command to clear orders
# @dp.message_handler(commands=["clear_orders"])
# async def clear_orders(message: types.Message):
#     user_id = message.from_user.id
#     if user_id in user_orders:
#         user_orders[user_id].clear()
#         await message.answer("🗑 Sizning buyurtmalaringiz tozalandi.")
#     else:
#         await message.answer("🛍 Sizning buyurtmalaringiz bo'sh.")
