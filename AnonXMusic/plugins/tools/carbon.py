import aiohttp
from io import BytesIO
from AnonXMusic import app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

EVAA = [
    [
        InlineKeyboardButton(text="✙ ʌᴅᴅ ϻє ɪη ʏσυʀ ɢʀσυᴘ ✙", url=f"https://t.me/TensionxMusicBot?startgroup=true"),
    ],
]


async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={"code": code}) as resp:
            image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image



@app.on_message(filters.command("carbon"))
async def _carbon(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply_text("<b>๏ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴀᴋᴇ ᴀ ᴄᴀʀʙᴏɴ</b>")
        return
    if not (replied.text or replied.caption):
        return await message.reply_text("<b>๏ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴀᴋᴇ ᴀ ᴄᴀʀʙᴏɴ</b>")
    text = await message.reply("<b>๏ ᴘʀᴏᴄᴇssɪɴɢ...</b>.")
    carbon = await make_carbon(replied.text or replied.caption)
    await text.edit(" <b>๏ ᴜᴘʟᴏᴀᴅɪɴɢ... </b>")
    await message.reply_photo(carbon, caption=f"<b>❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ ˹ ᴛᴇɴsɪᴏɴ ꭙ ᴍᴜsɪᴄ˼</b>", reply_markup=InlineKeyboardMarkup(EVAA),
    )
    await text.delete()
    carbon.close()
