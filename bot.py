# =========================
#   DISCORD BOT + WEB OK
# =========================

import discord
import os
import threading
from flask import Flask, request

# -------- CONFIG --------

TOKEN = os.getenv("TOKEN")  # ponelo como variable de entorno

PORT = int(os.getenv("PORT", 8080))

# -------- FLASK WEB --------

app = Flask("server")

@app.route("/")
def home():
    return "OK", 200

@app.route("/ping")
def ping():
    print("Ping recibido desde la web")
    return "OK", 200

def run_web():
    app.run(host="0.0.0.0", port=PORT)

# -------- DISCORD BOT --------

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
        activity=discord.Game("Conectado al servidor web")
    )

@client.event
async def on_disconnect():
    print("Bot desconectado... intentando reconectar")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.lower() == "!ping":
        await message.channel.send("OK")

# -------- START --------

if __name__ == "__main__":
    # Inicia web en segundo plano
    t = threading.Thread(target=run_web)
    t.daemon = True
    t.start()

    # Inicia bot
    client.run(TOKEN)
