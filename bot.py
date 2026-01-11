import discord

TOKEN = "PON_TU_TOKEN_AQUI"

intents = discord.Intents.default()
intents.members = True
intents.presences = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Bot conectado como", client.user)

client.run(TOKEN)
