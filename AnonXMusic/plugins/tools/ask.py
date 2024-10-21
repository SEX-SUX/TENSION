from pyrogram import Client, filters
import requests
from AnonXMusic import app 

# Define the model list
models_list = ['blackbox', 'gemini-1.5-flash', 'llama-3.1-405b', 'gpt-4o', 'gemini-pro', 'claude-sonnet-3.5']

# Set the default model
default_model = 'gpt-4o'

# Function to query the API
def query_model(message, model=default_model):
    api_url = f"https://chatwithai.codesearch.workers.dev/?chat={message}&model={model}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json().get("response", "No response from the model")
    else:
        return f"Error: {response.status_code}"

# Handler for the /ask command
@app.on_message(filters.command("ask"))
def ask_command(client, message):
    if len(message.command) < 2:
        message.reply_text("Please provide a query after the command.")
        return

    # Get the query from the message
    query = " ".join(message.command[1:])
    
    # Call the API with the query using the default model
    response = query_model(query)
    
    # Reply with the model's response
    message.reply_text(response)
