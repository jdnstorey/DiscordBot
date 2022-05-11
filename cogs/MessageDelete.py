import nextcord
from nextcord import Interaction
from nextcord.ext import commands

from settings.server_ids import testing_server_id


class MessageDelete(commands.Cog):

    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="delete", description="Deletes messages", guild_ids=[testing_server_id])
    @commands.has_permissions(manage_messages = True)
    async def delete_message(self, interaction: Interaction, limit: int):
        await interaction.channel.purge(limit = limit)
        await interaction.response.send_message(f'{limit} messages purged!', delete_after = 3)


def setup(client):
    client.add_cog(MessageDelete(client))
