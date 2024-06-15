import discord
from discord import app_commands
from config import DATA_MANAGER, LANGUAGE_MANAGER


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
    timeout = LANGUAGE_MANAGER.command_get("changelang", "timeout")
    embed = discord.Embed(
        title=LANGUAGE_MANAGER.command_get("changelang", "embed_title"),
        description=LANGUAGE_MANAGER.command_get("changelang", "embed_description"),
        color=discord.Color.blurple()
    )
    embed.set_footer(text=LANGUAGE_MANAGER.command_get("changelang", "embed_footer").format(timeout))
    view = discord.ui.View(timeout=timeout)
    x = LANGUAGE_MANAGER.languages
    x.remove(LANGUAGE_MANAGER.language)
    for lang in x:
        button = LanguageButton(
            lang=lang,
            style=discord.ButtonStyle.primary,
            emoji=LANGUAGE_MANAGER.get_flag(lang),
            custom_id=f"changelang_{lang}"
        )
        view.add_item(button)
    await interaction.response.send_message(embed=embed, view=view)


def setup(tree: app_commands.CommandTree, guild: discord.Object):
    tree.command(
        name=LANGUAGE_MANAGER.command_get("changelang", "command_name"),
        description=LANGUAGE_MANAGER.command_get("changelang", "description"),
        guild=guild
    )(changelang_command)
