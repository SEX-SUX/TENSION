import os
import random
import time
from AnonXMusic import app
import requests
from pyrogram.types import  Message
from pyrogram.types import InputMediaPhoto
from teambabyAPI import api
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup



EVAA = [
    [
        InlineKeyboardButton(text="˹ sυᴘᴘσʀᴛ ˼", url=f"https://t.me/SANATANI_SUPPORT"),
        InlineKeyboardButton(text="˹ ᴜᴘᴅᴀᴛᴇ's ˼", url=f"https://t.me/TENSION_TECH"),
    ],
    [
        InlineKeyboardButton(text="✙ ʌᴅᴅ ϻє ɪη ʏσυʀ ɢʀσυᴘ ✙", url=f"https://t.me/TensionxMusicBot?startgroup=true"),
    ],
]

@app.on_message(
    filters.command(
        ["chatgpt", "i", "ai", "ask", "gpt", "solve"],
        prefixes=["+", ".", "/", "-", "", "$", "#", "&", "A", "a"],
    )
)
async def chat_gpt(bot, message):
    
    try:
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "❍ ᴇxᴀᴍᴘʟᴇ :\n\n/chatgpt how to set any girl")
        else:
            a = message.text.split(' ', 1)[1]
            r=api.gemini(a)["results"]
            await message.reply_text(f" {r} \n\n❍ 𝗣𝗼𝘄𝗲𝗿𝗲𝗱 𝗕𝘆 : <a href=https://t.me/TENSION_TECH>𝝩‌𝞊‌𝝶𝘀𝝸𝝾‌𝝶‌ 𝗧𝞊‌𝗰𝗵</a>", reply_markup=InlineKeyboardMarkup(EVAA)
    except Exception as e:
        await message.reply_text(f"❍ ᴇʀʀᴏʀ: {e} ")
