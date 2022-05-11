import os

import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '!', intents = intents)


@client.event
async def on_ready():
    print('Bot logged in successfully!')


# ------------------------------ cogs --------------------------------
initial_extensions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3])

if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)
# ------------------------------ cogs --------------------------------

client.run('OTczNTkwMjM5MjIwMjM2Mzg5.GNQfSm.khLOGx0TX0uD88OxT6vKnpA-ZQdMsppJSPcBYI')
