import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/bb7e6f59b3db29b215446.jpg",
        caption=f"""**ðð¡ð¢ð¬ ðð¬ ððð¯ðð§ðð ð¥ððð¥ðð ð«ðð¦ ðð®ð¬ð¢ð ð¶ ðð¨ð­ ðð®ð§ ðð§ ðð«ð¢ð¯ðð­ð ð¥ ðð©ð¬ ð«ððð«ð¯ðð« ð ðððð¥ â¤ï¸ ðð¢ð ð¡ ðð®ðð¥ð¢ð­ð² ðð®ð¬ð¢ð ð§ ðð§ ðð ððð¯ðð¥ð¨ð©ðð ðð² = [Dhruba'ðð ð¬â¤ï¸](https://t.me/DhrubaXD)

ðð«ððð­ð¨ð« :- [â¨ ð ð¿'ð¦ðºð¢ð¸ð²ð¿ ð¬ ð](https://t.me/DhrubaXD)
ðð®ð©ð©ð¨ð«ð­ :- [â¨ Group â¤ï¸ð¸](https://t.me/Legend_K_Userbot)
ðð¢ð¬ðð®ð¬ð¬ :- [â¨  Tough ðð¹ð®ð» ð§](https://t.me/Legend_K_Userbot)
ðð¨ð®ð«ðð  :- [â¨  ðð¹ð¶ð°ð¸ âï¸ ð¥ð²ð½ð¼ ð](https://github.com/LEGENDARY-OS/AIMusicX)
We are tough:- [â¨ ðð¼ð¶ð» â¤ï¸ð¥](https://t.me/Legend_K_Userbot)

ðð ðð¨ð® ððð¯ð ðð§ð² ðð®ðð¬ð­ð¢ð¨ð§ð¬ ðð§ð ððð¥ð© ðð¡ðð§ ðð¦ ðð² ðð¨ð¬ð¬ = [ð ð¿'Dhruba ð¬ â¤ï¸](https://t.me/DhrubaXD)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¥ Já´ÉªÉ´ Há´Êá´ & Sá´á´á´á´Êá´ â¨", url=f"https://t.me/Legend_K_Userbot")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/8c3abf591121615cdef42.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð¥ CÊÉªá´á´ Má´ Tá´ Gá´á´ Rá´á´á´ ð", url=f"https://github.com/LEGENDARY-OS/AIMusicX")
                ]
            ]
        ),
    )
