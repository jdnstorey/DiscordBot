import nextcord
from nextcord import Interaction
from nextcord.ext import commands

from settings.server_ids import testing_server_id, polo_king


class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="ping", description="Calculates the bot's current response time", guild_ids=[testing_server_id, polo_king])
    async def ping_command(self, interaction: Interaction):
        string = f"{round(self.client.latency * 1000)}ms"
        await interaction.response.send_message("**Ping is " + string + "**", ephemeral = True)

def setup(client):
    client.add_cog(Ping(client))
