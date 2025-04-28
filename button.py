from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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

end = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Yakunlash", callback_data="finished")]
    ]
)

