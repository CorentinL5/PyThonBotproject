import datetime
import discord as discord
from discord import app_commands

with open("assets/token.txt", "r") as f:
    TOKEN = f.read().strip()
GUILD_ID = 1202606516675289168
ROLE_ID = 1233425063982665809


class ButtonView(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label="verify", style=discord.ButtonStyle.green, custom_id="role_button", emoji="✅")
    async def verify(self, interaction: discord.Interaction,):
        if type(client.role) is not discord.Role:
            client.role = interaction.guild.get_role(ROLE_ID)
        if client.role not in interaction.user.roles:
            await interaction.user.add_roles(client.role)
            await interaction.response.send_message(f"I have given you {client.role.mention}!", ephemeral=True)
        else:
            await interaction.response.send_message(f"You already have {client.role.mention}!", ephemeral=True)


class Aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = True  # we use this so the bot doesn't sync commands more than once
        self.added = False
        self.role = ROLE_ID

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:  # check if slash commands have been synced
            await tree.sync(guild=discord.Object(id=GUILD_ID))  
            # |-> guild specific: leave blank if global (global registration can take 1-24 hours)
            self.synced = True
        if not self.added:
            self.add_view(ButtonView())
            self.added = True
        print(f"We have logged in as {self.user}.")


client = Aclient()
tree = app_commands.CommandTree(client)


@tree.command(guild=discord.Object(id=GUILD_ID), name='tester', description='testing')
async def slash2(interaction: discord.Interaction):
    embed = discord.Embed(title="Hey", description=f"This is a test {interaction.user.mention}", color=0x00ff00)
    embed.set_thumbnail(url=interaction.user.avatar)
    await interaction.response.send_message(embed=embed, ephemeral=True, view=btn1)


@tree.command(guild=discord.Object(id=GUILD_ID), name='button', description='Launches a button!')
async def launch_button(interaction: discord.Interaction):
    embed = discord.Embed(title="Hey", description=f"This is a test {interaction.user.mention}", color=0x00ff00)
    await interaction.response.send_message(embed=embed, view=ButtonView())


client.run(TOKEN)
