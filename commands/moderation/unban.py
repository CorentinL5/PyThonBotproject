import discord
from discord import app_commands
from config import DATA_MANAGER


async def ban_command(interaction: discord.Interaction, user: discord.User, reason: str):
    await interaction.guild.ban(user, reason=reason)
    await interaction.response.send_message(f"{user.mention} a été banni pour la raison suivante : {reason}")


def setup(tree: app_commands.CommandTree, guild: discord.Object):
    tree.command(
        name="unban",
        description="Bannir un utilisateur",
        guild=guild
    )(ban_command)
