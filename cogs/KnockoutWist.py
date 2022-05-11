import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from numpy import random

from settings.server_ids import testing_server_id

score = 0

# ------------------------------ buttons --------------------------------
class Buttons(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)
        self.value = None



    @nextcord.ui.button(label = "Stick", style = nextcord.ButtonStyle.red)
    async def stick(self, button: nextcord.ui.Button, interaction: Interaction):
        view = Buttons()
        global score

        print(3)

        # self.value = 'stick'

        await interaction.followup.send(f'You have chosen to stick, your final score is **{score}**')
        print(4)

        return



    @nextcord.ui.button(label="Hit", style=nextcord.ButtonStyle.blurple)
    async def hit(self, button: nextcord.ui.Button, interaction: Interaction):
        view = Buttons()
        global score

        print(5)
        # self.value = 'hit'

        score += (random.randint(12) + 1)
        print(6)
        await interaction.edit(content=f'Current score is **{score}**. Would you like to stick or hit?', view=view)
        print(7)
        return
# ------------------------------ buttons --------------------------------


# ------------------------------ game --------------------------------
class KnockoutWist(commands.Cog):
    def __init__(self, client): self.client = client

    @nextcord.slash_command(name="knockoutwist", description="Play the game Knockout Wist", guild_ids=[testing_server_id])
    async def reaction_roles_command(self, interaction: Interaction):
        global score

        view = Buttons()
        print(1)
        await interaction.response.send_message(f'Current score is **{score}**. Would you like to stick or hit?', view = view)
        print(2)

# ------------------------------ game --------------------------------


def setup(client):
    client.add_cog(KnockoutWist(client))
