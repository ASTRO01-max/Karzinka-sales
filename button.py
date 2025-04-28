from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from data_products import *

start = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Boshlash", callback_data="start_pressed")]
    ]
)

prev = InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_to_start")

main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🥗 Oziq-ovqatlar", callback_data="menu_foods")],
        [InlineKeyboardButton(text="📱 Elektronika", callback_data="menu_electronics")],
        [prev]
    ]
)

# food_menu = InlineKeyboardMarkup()
# for name, info in food_products.items():
#     btn = InlineKeyboardButton(text=name, callback_data=f"food_{name}")
#     food_menu.add(btn)
# food_menu.add(InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_to_main_menu"))

# electronic_menu = InlineKeyboardMarkup()
# for name, info in electronic_products.items():
#     btn = InlineKeyboardButton(text=name, callback_data=f"electronic_{name}")
#     electronic_menu.add(btn)
# electronic_menu.add(InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_to_main_menu"))

# purchase = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text="Sotib olish", callback_data="buy")]
#     ]
# )

end = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Yakunlash", callback_data="finished")]
    ]
)

