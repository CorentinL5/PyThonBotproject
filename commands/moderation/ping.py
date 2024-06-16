import discord
from discord import app_commands
from config import DATA_MANAGER, LANGUAGE_MANAGER


async def ping_command(interaction: discord.Interaction):
    ping = round(interaction.client.latency * 1000)
    await interaction.response.send_message(LANGUAGE_MANAGER.command_get("ping", "message").format(ping))
    message = await interaction.original_response()
    await message.add_reaction("🏓")


def setup(tree: app_commands.CommandTree, guild: discord.Object):
    tree.command(
        name=LANGUAGE_MANAGER.command_get("ping", "command_name"),
        description=LANGUAGE_MANAGER.command_get("ping", "command_description"),
        guild=guild
    )(ping_command)
