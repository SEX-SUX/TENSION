import os
import asyncio
from pyrogram import Client, filters
import aiohttp
from AnonXMusic import app 
# Define the API endpoint
API_URL = "https://chatwithai.codesearch.workers.dev/?chat={message}&model=gpt-4o"

@app.on_message(filters.command("ask"))
async def ask(client, message):
    # Extract the query after the command
    query = message.text.split(" ", 1)[1] if len(message.text.split(" ")) > 1 else ""
    
    if not query:
        await message.reply("Please provide a query after the command.")
        return

    # Send the request to the API
    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL.format(message=query)) as response:
            if response.status == 200:
                data = await response.json()
                # Assuming the response contains a field 'reply' with the AI's answer
                answer = data.get("reply", "No response from the model.")
            else:
                answer = "Failed to get a response from the AI."

    # Send the answer back to the Telegram chat
    await message.reply(answer)
