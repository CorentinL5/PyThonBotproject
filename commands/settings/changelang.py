import discord
from discord import app_commands
from config import DATA_MANAGER, LANGUAGE_MANAGER, NO_PERM_EMBED
import asyncio


class LanguageButton(discord.ui.Button):
    def __init__(self, lang, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lang = lang

    async def callback(self, interaction: discord.Interaction):
        LANGUAGE_MANAGER.set_lang(self.lang, interaction.guild.id)
        DATA_MANAGER.set_server_info(interaction.guild.id, "lang", self.lang)
        await interaction.response.edit_message(
            embed=discord.Embed(
                title=LANGUAGE_MANAGER.command_get("changelang", "embed_title"),
                description=LANGUAGE_MANAGER.command_get("changelang", "success").format(self.lang),
                color=discord.Color.green()
            ),
            view=None
        )


async def changelang_command(interaction: discord.Interaction):
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message(embed=NO_PERM_EMBED(interaction.command.name), ephemeral=True)
        return
    timeout = LANGUAGE_MANAGER.command_get("changelang", "timeout")
    embed = discord.Embed(
        title=LANGUAGE_MANAGER.command_get("changelang", "embed_title"),
        description=LANGUAGE_MANAGER.command_get("changelang", "embed_description"),
        color=discord.Color.blurple(),
        timestamp=discord.utils.utcnow()
    )
    view = discord.ui.View(timeout=timeout)
    for lang in LANGUAGE_MANAGER.languages:
        button = LanguageButton(
            lang=lang,
            style=discord.ButtonStyle.primary,
            emoji=LANGUAGE_MANAGER.get_flag(lang),
            custom_id=f"changelang_{lang}",
            disabled=lang == DATA_MANAGER.get_server_info(interaction.guild.id, "lang")
        )
        view.add_item(button)
    await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
    message = await interaction.original_response()
    await view.wait()
    await message.edit(view=None)


def setup(tree: app_commands.CommandTree, guild):
    tree.command(
        name=LANGUAGE_MANAGER.command_get("changelang", "command_name"),
        description=LANGUAGE_MANAGER.command_get("changelang", "command_description"),
        guild=guild
    )(changelang_command)
