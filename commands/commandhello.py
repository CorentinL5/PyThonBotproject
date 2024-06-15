import discord
from discord import app_commands
from config import GUILD_ID, BOT_LOGO_ATTACHMENT, BOT_LOGO, LANGUAGE_MANAGER


async def helloworld(interaction: discord.Interaction):
    embed = discord.Embed(
        title=LANGUAGE_MANAGER.command_get("helloworld", "embed_title"),
        description=LANGUAGE_MANAGER.command_get("helloworld", "embed_description".format(interaction.user)),
        color=discord.Color.blurple()
    )
    embed.set_thumbnail(url=BOT_LOGO_ATTACHMENT)

    await interaction.response.send_message(embed=embed, file=BOT_LOGO, ephemeral=True)


def setup(tree: app_commands.CommandTree, guild: discord.Object):
    tree.command(
        name=LANGUAGE_MANAGER.command_get("helloworld", "command_name"),
        description=LANGUAGE_MANAGER.command_get("helloworld", "description"),
        guild=guild
    )(helloworld)
