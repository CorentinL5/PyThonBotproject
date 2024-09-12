import discord
from discord import app_commands
from config import DATA_MANAGER, LANGUAGE_MANAGER, NO_PERM_EMBED


async def unban_command(interaction: discord.Interaction, user: discord.User, reason: str = None):
    # check if user has permission to ban/unban members
    if not interaction.user.guild_permissions.ban_members:
        await interaction.response.send_message(embed=NO_PERM_EMBED(interaction.command.name), ephemeral=True)
        return

    if reason is None:
        reason = LANGUAGE_MANAGER.command_get("unban", "default_reason")

    embed = discord.Embed(
        title=LANGUAGE_MANAGER.command_get("unban", "embed_title").format(user.name),
        description=LANGUAGE_MANAGER.command_get("unban", "embed_description").format(reason),
        timestamp=discord.utils.utcnow(),
        color=discord.Color.red()
    )

    try:
        await interaction.guild.unban(user, reason=reason)
    except discord.NotFound:
        embed.description = LANGUAGE_MANAGER.command_get("unban", "not_banned").format(user.mention)
    except Exception as e:
        if user.bot:
            embed.description = LANGUAGE_MANAGER.command_get("error", "is_bot")
        else:
            embed.description = LANGUAGE_MANAGER.command_get("error", "try_error").format(interaction.command.name)
            print(e)
    finally:
        await interaction.response.send_message(embed=embed, ephemeral=True)


def setup(tree: app_commands.CommandTree, guild):
    tree.command(
        name=LANGUAGE_MANAGER.command_get("unban", "command_name"),
        description=LANGUAGE_MANAGER.command_get("unban", "command_description"),
        guild=guild
    )(unban_command)
