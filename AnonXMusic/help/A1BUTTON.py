from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

import config
from NEXIOMUSIC import app

class BUTTONS(object):
    MBUTTON = [
        [
            InlineKeyboardButton("˹ 🇸ʌᷟᴄᷣʜɪ֟፝η ˼", url="https://t.me/V_VIP_OWNER")
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
            
        ]
        ]
    
    SBUTTON = [
 
        [
            InlineKeyboardButton("sᴧηᴧᴛᴧηɪ ᴛєᴄʜ", url="https://t.me/ALL_SANATANI_BOT"),
        ],
        [
            InlineKeyboardButton("ϻσση ʜυɢ", url="https://t.me/MOON_HUB"),
            InlineKeyboardButton("ηєxɪσ ᴛєᴄʜ", url="https://t.me/NEXIO_TECH"),
        ],
        [
            InlineKeyboardButton("ᴄʜᴧᴛ ɢᴄ", url="https://t.me/SANATANI_SUPPORT"),
            InlineKeyboardButton("ᴛєηsɪση ᴛєᴄʜ", url="https://t.me/THE_TENSION"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
            
        ]
        ]
    
    ABUTTON = [
        [
            InlineKeyboardButton("ᴧʙσυᴛ", url="https://t.me/II_SANATANI_II"),
            InlineKeyboardButton("ʜєʟᴘ | ɪηғσ", callback_data="settings_back_helper"),
        ],
        [
            InlineKeyboardButton("ʙᴧsɪᴄ ɢυɪᴅє", callback_data="ABOUT_BACK HELP_GUIDE"),
            InlineKeyboardButton("ᴅσηᴧᴛє", callback_data="ABOUT_BACK HELP_DONATE"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
            
        ]
        ]
