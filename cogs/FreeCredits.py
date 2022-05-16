import json
from numpy import random

import nextcord
from nextcord import Interaction
from nextcord.ext import commands

from UserData.GetUserData import *
from settings.server_ids import testing_server_id, polo_king

class FreeCredits(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="free", description="Gives members 100 free credits", guild_ids=[testing_server_id, polo_king])
    async def free_credits(self, interaction: Interaction):
        # load balance from file

        if open_file_free_credits(interaction.user.id) is True:
            # user has already claimed
            await interaction.response.send_message(f"{interaction.user.mention}, you have already claimed your free credits!")
        else:
            # add 100 credits
            write_file_balance(interaction.user.id, 100)
            await interaction.response.send_message(f"100 credits has been added to {interaction.user.mention}'s account!")


def setup(client):
    client.add_cog(FreeCredits(client))
