import nextcord
from nextcord import Interaction
from nextcord.ext import commands

from settings.server_ids import testing_server_id, polo_king

class HelpModal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(
            "Help Form"
        )
        self.emTitle = nextcord.ui.TextInput(label="Help Form - Title", min_length=5, max_length=100, required=True, placeholder="What is the title of your problem?")
        self.add_item(self.emTitle)

        self.emDescription = nextcord.ui.TextInput(label="Help Form - Description", min_length=50, max_length=2000, required=True, placeholder="What is your problem?", style=nextcord.TextInputStyle.paragraph)
        self.add_item(self.emDescription)

    async def callback(self, interaction: Interaction) -> None:
        title = self.emTitle.value
        desc = self.emDescription.value
        em = nextcord.Embed(title = title, description = desc)
        return await interaction.response.send_message(embed=em)

class HelpForm(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="help", description="Opens a help form", guild_ids=[testing_server_id, polo_king])
    async def help_form(self, interaction: Interaction):
        await interaction.response.send_modal(HelpModal())

def setup(client):
    client.add_cog(HelpForm(client))
