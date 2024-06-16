import discord
from discord import app_commands
from config import DATA_MANAGER, LANGUAGE_MANAGER, TREE, CLIENT


async def help_command(interaction: discord.Interaction):
    embeds = []
    commands_list = TREE.get_commands(guild=interaction.guild)
    chunk_size = 5

    for i in range(0, len(commands_list), chunk_size):
        embed = discord.Embed(
            title=LANGUAGE_MANAGER.command_get("help", "embed_title"),
            description=LANGUAGE_MANAGER.command_get("help", "embed_description"),
            color=discord.Color.blurple()
        )
        chunk = commands_list[i:i + chunk_size]
        for command in chunk:
            embed.add_field(
                name=LANGUAGE_MANAGER.command_get("help", "embed_field_title").format(command.name),
                value=LANGUAGE_MANAGER.command_get("help", "embed_field_value").format(command.description),
                inline=False
            )
        embeds.append(embed)

    await interaction.response.send_message(embed=embeds[0])
    message = await interaction.original_response()
    await message.add_reaction("⬅️")
    await message.add_reaction("➡️")

    current_page = 0

    def check(check_reaction, check_user):
        return (check_user ==
                interaction.user
                and str(check_reaction.emoji)
                in ["⬅️", "➡️"]
                and check_reaction.message.id == message.id)

    while True:
        try:
            reaction, user = await CLIENT.wait_for("reaction_add", timeout=60.0, check=check)

            if str(reaction.emoji) == "➡️":
                current_page += 1
                if current_page >= len(embeds):
                    current_page = 0
            elif str(reaction.emoji) == "⬅️":
                current_page -= 1
                if current_page < 0:
                    current_page = len(embeds) - 1

            await message.edit(embed=embeds[current_page])
            await message.remove_reaction(reaction, user)
        except asyncio.TimeoutError:
            break


def setup(tree: app_commands.CommandTree, guild: discord.Object):
    tree.command(
        name=LANGUAGE_MANAGER.command_get("help", "command_name"),
        description=LANGUAGE_MANAGER.command_get("help", "command_description"),
        guild=guild
    )(help_command)
