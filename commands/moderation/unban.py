import discord
from discord import app_commands
from config import DATA_MANAGER, LANGUAGE_MANAGER


async def unban_command(interaction: discord.Interaction, user: discord.User):
    await interaction.guild.unban(user)
    await interaction.response.send_message(LANGUAGE_MANAGER.command_get("unban", "message").format(user.name))


def setup(tree: app_commands.CommandTree, guild: discord.Object):
    tree.command(
        name=LANGUAGE_MANAGER.command_get("unban", "command_name"),
        description=LANGUAGE_MANAGER.command_get("unban", "command_description"),
        guild=guild
    )(unban_command)
