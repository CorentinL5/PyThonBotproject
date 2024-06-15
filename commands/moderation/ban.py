import discord
from discord import app_commands
from config import DATA_MANAGER, LANGUAGE_MANAGER

async def ban_command(interaction: discord.Interaction, user: discord.User, reason: str):
    await interaction.guild.ban(user, reason=reason)
    await interaction.response.send_message(LANGUAGE_MANAGER.command_get("ban", "message").format(user.mention, reason), ephemeral=True)

def setup(tree: app_commands.CommandTree, guild: discord.Object):
    tree.command(
        name=LANGUAGE_MANAGER.command_get("ban", "command_name"),
        description=LANGUAGE_MANAGER.command_get("ban", "description"),
        guild=guild
    )(ban_command)