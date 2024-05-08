from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from ARYAN import app
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from ARYAN.core.userbot import Userbot
from pyrogram import Client, filters
from ARYAN import app
import asyncio
import random
from pyrogram import Client, filters



@Client.on_message(filters.command("repo") & filters.group)
async def repo(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/7ec3b010624cc49644454.jpg",
        caption=f"""ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url=f"https://github.com/THEMADMAXPRO/ARYANMUSIC"
                    )
                ]
            ]
        ),
    )


@Client.on_message(filters.command("repo") & filters.group)
async def help(client: Client, message: Message):

    await message.reply_photo(
        photo=f"https://te.legra.ph/file/7ec3b010624cc49644454.jpg",
        caption=f"""ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url=f"https://github.com/THEMADMAXPRO/ARYANMUSIC"
                    )
                ]
            ]
        ),
    )


@Client.on_message(filters.command("repo") & filters.private)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/7ec3b010624cc49644454.jpg",
        caption=f"""ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url=f"https://github.com/THEMADMAXPRO/ARYANMUSIC"
                    )
                ]
            ]
        ),
    )


