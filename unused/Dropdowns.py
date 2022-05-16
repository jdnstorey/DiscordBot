import nextcord
from nextcord.ext import commands
from nextcord import Interaction

from settings.server_ids import testing_server_id, polo_king


class Dropdown(nextcord.ui.Select):
    def __init__(self):
        service_type = [
            nextcord.SelectOption(label='Report a user', description=''),
            nextcord.SelectOption(label='Ask a mod a question', description=''),
            nextcord.SelectOption(label='Request a role', description='')
        ]
        super().__init__(placeholder="Service Types", min_values=1, max_values=1, options=service_type)

    # async def callback(self, interaction: Interaction):
    #    if self.values[0] == "Report a user":
    #        return await interaction.response.send_message("Which member would you like to report? Please do @<username>#<discriminator>")

    #    elif self.values[0] == "Ask a mod a question":
    #        return await interaction.response.send_message("What is your question?")

    #    else:
    #        return await interaction.response.send_message("Which role would you like?")


class DropdownView(nextcord.ui.View):
    def __init__(self):
        super().__init__()
    #    self.add_item(Dropdown())


class Dropdowns(commands.Cog):
    def __init__(self, client):
        self.client = client

    # @nextcord.slash_command(name="help", description="Request a help service",guild_ids=[testing_server_id, polo_king])
    # async def help_command(self, interaction: Interaction):
    #    view = DropdownView()
    #    await interaction.response.send_message("What help service would you like?", view = view, ephemeral=True)


def setup(client):
    client.add_cog(Dropdowns(client))
