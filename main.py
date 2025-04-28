import asyncio
import logging
import sys

from aiogram import Bot, html, Dispatcher, F, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.keyboard import InlineKeyboardBuilder
from button import *
from data_products import *

TOKEN = "8017218888:AAHepLMKZVM8CK0RugfxQrUxznxH5Q155FY"
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

def get_electronics_cart_keyboard():
    builder = InlineKeyboardBuilder()

    for key in electronic_products.keys():
        builder.button(text=key, callback_data=f"product_electronics:{key}")

    builder.button(text="⬅️ Orqaga", callback_data="back_to_start")
    builder.adjust(1)
    return builder.as_markup()

def get_foods_cart_keyboard():
    builder = InlineKeyboardBuilder()

    for key in food_products.keys():
        builder.button(text=key, callback_data=f"product_foods:{key}")

    builder.button(text="⬅️ Orqaga", callback_data="back_to_start")
    builder.adjust(1)
    return builder.as_markup()

@dp.message(CommandStart())
async def command_start(message: types.Message):
    await message.answer(
        f"Assalomu alaykum, botga xush kelibsiz {html.bold(message.from_user.full_name)}!"
    )
    await message.answer(
        "Botni ishga tushirish uchun 'Boshlash' tugmasini bosing 👇",
        reply_markup=start  
    )

@dp.callback_query(F.data == "start_pressed")
async def send_menu(callback_query: types.CallbackQuery):
    await callback_query.message.answer(
        text="Quyidagilardan birini tanlang:",
        reply_markup=main_menu 
    )
    await callback_query.answer()

@dp.callback_query(F.data == "menu_electronics")
async def electronics_menu(callback_query: types.CallbackQuery):
    await callback_query.message.answer(
        text="Elektron mahsulotlar:",
        reply_markup=get_electronics_cart_keyboard()
    )
    await callback_query.answer()

@dp.callback_query(F.data == "menu_foods")
async def foods_menu(callback_query: types.CallbackQuery):
    await callback_query.message.answer(
        text="Oziq-ovqat mahsulotlari:",
        reply_markup=get_foods_cart_keyboard()
    )
    await callback_query.answer()

@dp.callback_query(F.data.startswith("product_electronics:"))
async def product_info_electronics(callback_query: types.CallbackQuery):
    product_name = callback_query.data.split(":", 1)[1]
    product = electronic_products.get(product_name)

    if product:
        text = (
            f"📦 Mahsulot nomi: {product['📦 Mahsulot nomi']}\n"
            f"Narxi💵: {product['💵 Narxi']}"
        )
        builder = InlineKeyboardBuilder()
        builder.button(text="🛒Sotib olish", callback_data="buy")
        builder.button(text="⬅️ Orqaga", callback_data="back_to_start")
        builder.adjust(1)
        await callback_query.message.answer(text, reply_markup=builder.as_markup())
    else:
        await callback_query.message.answer("Mahsulot topilmadi.")
    await callback_query.answer()

@dp.callback_query(F.data.startswith("product_foods:"))
async def product_info_foods(callback_query: types.CallbackQuery):
    product_name = callback_query.data.split(":", 1)[1]
    product = food_products.get(product_name)

    if product:
        text = (
            f"📦 Mahsulot nomi: {product['📦 Mahsulot nomi']}\n"
            f"Narxi💵: {product['💵 Narxi']}"
        )
        builder = InlineKeyboardBuilder()
        builder.button(text="🛒Sotib olish", callback_data="buy")
        builder.button(text="⬅️ Orqaga", callback_data="back_to_start")
        builder.adjust(1)
        await callback_query.message.answer(text, reply_markup=builder.as_markup())
    else:
        await callback_query.message.answer("Mahsulot topilmadi.")
    await callback_query.answer()

@dp.callback_query(F.data == "buy")
async def purchase(callback_query: types.CallbackQuery):
    product_name = callback_query.message.text.split("\n")[0].replace("📦 Mahsulot nomi: ", "")
    product_price = callback_query.message.text.split("\n")[1].replace("Narxi💵: ", "")

    await callback_query.message.answer(
        f"Buyurtmangiz qabul qilindi!\n\nMahsulot: {product_name}\nNarxi: {product_price}"
    )
    
    builder = InlineKeyboardBuilder()
    builder.button(text="Bosh sahifaga", callback_data="back_to_start")
    builder.adjust(1)
    
    await callback_query.message.answer("Buyurtma muvaffaqiyatli amalga oshirildi!", reply_markup=builder.as_markup())

@dp.callback_query(F.data == "back_to_start")
async def back_menu(callback_query: types.CallbackQuery):
    await callback_query.message.answer(
        text="Quyidagilardan birini tanlang:",
        reply_markup=main_menu  
    )
    await callback_query.answer()

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
