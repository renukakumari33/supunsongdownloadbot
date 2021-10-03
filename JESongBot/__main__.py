#Music Factory <https://t.me/ankimusicgroup>


from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from JESongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from JESongBot import Jebot as app
from JESongBot import LOGGER

pm_start_text = """
Hey [{}](tg://user?id={}), I'm Music Factory Song Downloader Bot 🎵

😉 Just send me the song name you want to download.😋
      eg:```/song alone```
      
A bot by @tujan2 👈
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        text="🎵 Our Music Group 🎵", url="https://t.me/ankimusicgroup"
                    ),
                    InlineKeyboardButton(
                        text="Our Rap Bot", url="@thisbotx_bot"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info(" mySongBot is online.")
idle()
