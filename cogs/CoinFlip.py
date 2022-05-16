import json

import nextcord
from nextcord import Interaction
from nextcord.ext import commands

from numpy import random

from UserData.GetUserData import *
from settings.server_ids import testing_server_id, polo_king

class CoinFlip(commands.Cog):

    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="coinflip", description="Plays a game of coinflip", guild_ids=[testing_server_id, polo_king])
    async def coinflip(self, interaction: Interaction, amount: int):
        balance = open_file_balance(interaction.user.id)
        uuid_balance = int(balance)

        if uuid_balance is None:
            await interaction.response.send_message(
                f"{interaction.user.mention}'s current balance is empty. Please do /free to receive 100 free credits!")
        else:
            if uuid_balance < amount:
                await interaction.response.send_message(f'Insufficient Balance. You have **{uuid_balance}** credits remaining')
            elif uuid_balance >= amount:
                rand = random.randint(12)

                if rand < 6:
                    uuid_balance -= amount
                    write_file_balance(uuid=interaction.user.id, balance=str(uuid_balance))
                    await interaction.response.send_message(f'**{amount} credits lost**! You have {uuid_balance} credits remaining', delete_after = 3)
                    return
                else:
                    uuid_balance += amount
                    write_file_balance(uuid = interaction.user.id, balance = str(uuid_balance))
                    await interaction.response.send_message(f'**{amount} credits won**! You have {uuid_balance} credits remaining', delete_after = 3)
                    return

def setup(client):
    client.add_cog(CoinFlip(client))
