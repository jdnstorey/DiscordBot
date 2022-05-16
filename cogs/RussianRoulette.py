import json
from numpy import random

import nextcord
from nextcord import Interaction
from nextcord.ext import commands

from UserData.GetUserData import *
from settings.server_ids import testing_server_id, polo_king

def maths(uuid: int):
    r = (random.randint(5) + 1)
    return r

class RussianRoulette(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="russianroulette", description="Plays a game of russian roulette", guild_ids=[testing_server_id, polo_king])
    async def russian_roulette(self, interaction: Interaction, bet_amount: int, shot_guess: int):
        # load balance from file
        uuid_balance = open_file_balance(interaction.user.id)

        #if uuid_balance is None:
        #    await interaction.edit(content=f"{interaction.user.mention}'s current balance is empty. Please do /free to receive 100 free credits!")
        #else:
        #    await interaction.edit(content=f"{interaction.user.mention}'s current balance is {uuid_balance} credits!")

        m = maths(interaction.user.id)
        print(m)

        if shot_guess is not m:
            # win condition
            uuid_balance += bet_amount
            write_file_balance(interaction.user.id, uuid_balance)
            await interaction.response.send_message(f"{interaction.user.mention} survived! You have won {bet_amount} credits. Your new balance is {uuid_balance}!")
        else:
            # lose condition
            uuid_balance -= bet_amount
            write_file_balance(interaction.user.id, uuid_balance)
            await interaction.response.send_message(f"{interaction.user.mention} was shot in the head! You have lost {bet_amount} credits. Your new balance is {uuid_balance}!")


def setup(client):
    client.add_cog(RussianRoulette(client))
