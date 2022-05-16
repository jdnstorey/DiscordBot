import json

import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from numpy import random

from UserData.GetUserData import *
from settings.server_ids import testing_server_id, polo_king

amount = 0

# ------------------------------ maths --------------------------------
def maths(uuid: int):
    r = (random.randint(7) + 15)
    d = open_file_blackjack(uuid)
    if r > d:
        return "lose"
    elif r < d:
        return "win"
    else:
        return "draw"

def starting_score(uuid: int):
    r = (random.randint(14) + 1)
    return r
# ------------------------------ maths --------------------------------


# ------------------------------ buttons --------------------------------
class PlayAgain(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)
        self.value = None

    @nextcord.ui.button(label="Play Again", style=nextcord.ButtonStyle.green)
    async def play_again(self, button: nextcord.ui.Button, interaction: Interaction):
        # load hit and stick buttons
        view = Buttons()

        #read score from file
        score = open_file_blackjack(interaction.user.id)

        # calculate starting score
        s = starting_score(interaction.user.id)

        #write to file
        write_file_blackjack(interaction.user.id, s)

        # send chat output
        await interaction.edit(content=f'Current score is **{s}**. Would you like to stick or hit?', view=view)
        return

class Buttons(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)
        self.value = None

    @nextcord.ui.button(label = "Stick", style = nextcord.ButtonStyle.red)
    async def stick(self, button: nextcord.ui.Button, interaction: Interaction):
        # load play again button
        playagain = PlayAgain()

        # read score and balance
        score = open_file_blackjack(interaction.user.id)
        balance = open_file_balance(interaction.user.id)

        # calculate robot card value
        m = maths(interaction.user.id)

        if m == "win":
            if score == 21:
                write_file_balance(interaction.user.id, int(balance * 1.2))
                await interaction.edit(content = f'You have chosen to stick, and won! You have gained {int(balance * 0.2)} credits. Would you like to play again?',view=playagain)
            else:
                write_file_balance(interaction.user.id, int(balance * 1.1))
                await interaction.edit(content = f'You have chosen to stick, and won! You have gained {int(balance * 0.1)} credits. Would you like to play again?', view=playagain)

        elif m == "lose":
            write_file_balance(interaction.user.id, int(balance * 0.9))
            await interaction.edit(content = f'You have chosen to stick, and lost! You have lost {int(balance * 0.1)} credits. Would you like to play again?', view=playagain)

        elif m == "draw":
            write_file_balance(interaction.user.id, int(balance * 1))
            await interaction.edit(content = f'You have chosen to stick, and drawn! Would you like to play again?', view=playagain)

        s = starting_score(interaction.user.id)
        write_file_blackjack(interaction.user.id, s)
        return


    @nextcord.ui.button(label="Hit", style=nextcord.ButtonStyle.blurple)
    async def hit(self, button: nextcord.ui.Button, interaction: Interaction):
        # load buttons
        view = Buttons()
        playagain = PlayAgain()

        # load score, balance and create integer of the balance
        score = open_file_blackjack(interaction.user.id)
        balance = open_file_balance(interaction.user.id)
        uuid_balance = int(balance)

        # calculate 'hit' score to add
        score += (random.randint(9) + 1)
        write_file_blackjack(uuid=interaction.user.id, score=score)

        if score > 21:  # if going bust
            # update score
            uuid_balance -= int(uuid_balance * 0.25)

            # remove 10% of credits
            write_file_balance(uuid=interaction.user.id, balance=uuid_balance)

            # message
            await interaction.edit(content = f"You have gone bust! You lost {int(uuid_balance * 0.25)} credits! Your current balance is {uuid_balance}, would you like to play again?", view = playagain)
        else:
            # message
            await interaction.edit(content=f'Current score is **{score}**. Would you like to stick or hit?', view=view)
            return
# ------------------------------ buttons --------------------------------


# ------------------------------ game --------------------------------
class BlackJack(commands.Cog):
    def __init__(self, client): self.client = client

    @nextcord.slash_command(name="blackjack", description="Play the game BlackJack", guild_ids=[testing_server_id, polo_king])
    async def blackjack_command(self, interaction: Interaction):
        # load buttons
        view = Buttons()

        # load score from file, and calculate starting score
        score = open_file_blackjack(interaction.user.id)
        s = starting_score(interaction.user.id)

        # load balance from file
        uuid_balance = open_file_balance(interaction.user.id)

        if uuid_balance is None:
            await interaction.response.send_message(
                f"{interaction.user.mention}'s current balance is empty. Please do /free to receive 100 free credits!")
        else:
            # if user doesn't exist in file
            if score is None:
                # assign starting score
                write_file_blackjack(uuid=interaction.user.id, score=s)
                await interaction.response.send_message(f"{interaction.user.mention}'s current score is {s}!")
            else:
                # if score in file is above 21
                if score > 21:
                    # replace local score with starting score
                    write_file_blackjack(uuid=interaction.user.id, score=s)
            await interaction.response.send_message(f'Current score is **{s}**. Would you like to stick or hit?', view = view)

# ------------------------------ game --------------------------------


def setup(client):
    client.add_cog(BlackJack(client))
