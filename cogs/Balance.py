import json

import nextcord
from nextcord import Interaction
from nextcord.ext import commands

from UserData.GetUserData import *
from settings.server_ids import testing_server_id, polo_king

class Balance(commands.Cog):

    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="balance", description="Displays the user's current balance", guild_ids=[testing_server_id, polo_king])
    async def balance(self, interaction: Interaction):
        uuid_balance = open_file_balance(interaction.user.id)
        if uuid_balance is None:
            await interaction.response.send_message(f"{interaction.user.mention}'s current balance is empty. Please do /free to receive 100 free credits!")
        else:
            await interaction.response.send_message(f"{interaction.user.mention}'s current balance is {uuid_balance} credits!")

    @nextcord.slash_command(name="balance_modify",  description="Edit a user's balance", guild_ids=[testing_server_id, polo_king])
    @commands.has_permissions(administrator=True)
    async def balance_modify(self, interaction: Interaction, user: nextcord.User, balance: str):
        uuid = user.id
        bal = open_file_balance(uuid)
        bal += int(balance)
        write_file_balance(uuid, bal)
        await interaction.response.send_message(f'{balance} credits sent to {user}', ephemeral=True)


def setup(client):
    client.add_cog(Balance(client))
