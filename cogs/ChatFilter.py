from nextcord.ext import commands

from settings.banned_words import banned_words


class ChatFilter(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        for word in banned_words:
            if word in message.content.lower():
                await message.channel.purge(limit=1)
                await message.channel.send(f'{message.author.mention}! No foul language!', delete_after = 2)

        else:
            return

def setup(client):
    client.add_cog(ChatFilter(client))
