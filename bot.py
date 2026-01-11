# =====================================
#   DISCORD BOT + WEB SERVER (REPLIT)
# =====================================

import discord
import threading
from flask import Flask

# ----------- CONFIG -----------

TOKEN = "PEGA_TU_TOKEN_AQUI"
PORT = 8080

# ----------- WEB (REPLIT) -----------

app = Flask("server")

@app.route("/")
def home():
    return "OK"

@app.route("/ping")
def ping():
    print("Ping recibido desde Replit web")
    return "OK"

def run_web():
    app.run(host="0.0.0.0", port=PORT)

# ----------- DISCORD BOT -----------

intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("=================================")
    print("BOT CONECTADO COMO:", client.user)
    print("=================================")
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Game("Replit conectado")
    )

@client.event
async def on_disconnect():
    print("Bot desconectado... Discord lo va a reconectar solo")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.lower() == "!ping":
        await message.channel.send("OK desde Replit")

# ----------- START -----------

t = threading.Thread(target=run_web)
t.daemon = True
t.start()

client.run(TOKEN)
