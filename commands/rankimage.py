import discord
from discord import app_commands
from config import DATA_MANAGER, LANGUAGE_MANAGER
from generate_rank_image import generate_rank_image


async def rankimage_command(interaction: discord.Interaction):
    b_level = DATA_MANAGER.get_user_info(interaction.guild.id, interaction.user.id, "level")
    b_xp = DATA_MANAGER.get_user_info(interaction.guild.id, interaction.user.id, "xp")

    if b_level is not None:
        cmd_level = b_level
    else:
        cmd_level = 1
        DATA_MANAGER.set_user_info(interaction.guild.id, interaction.user.id, "level", cmd_level)
    if b_xp is not None:
        cmd_xp = b_xp
    else:
        cmd_xp = 0
        DATA_MANAGER.set_user_info(interaction.guild.id, interaction.user.id, "xp", cmd_xp)

    image = generate_rank_image(
        avatar_url=f"{interaction.user.avatar}?size=256",
        level=cmd_level,
        xp=cmd_xp
    )
    await interaction.response.send_message(
        file=discord.File(fp=image, filename="rank_image.png")
    )


def setup(tree: app_commands.CommandTree, guild):
    tree.command(
        name="rank",  # LANGUAGE_MANAGER.command_get("rankimage", "command_name"),
        description="rank desc",  # LANGUAGE_MANAGER.command_get("rankimage", "description"),
        guild=guild
    )(rankimage_command)
