import os
import discord
from config import (CLIENT, TREE, LANGUAGE_MANAGER, TOKEN, MY_GUILD,
                    COMMANDS_DIRECTORIES, COMMANDS_DIRECTORY, MODULE_TREE, IN_DEV_MODE)


# Load all commands
for directory in COMMANDS_DIRECTORIES:
    for filename in os.listdir(directory):
        if filename.endswith('.py') and filename != '__init__.py':
            if directory == COMMANDS_DIRECTORY:
                module_name = filename[:-3]
            else:
                directory = directory.replace(COMMANDS_DIRECTORY[1:], '').replace('/', '.')
                module_name = f'{directory[2:]}.{filename[:-3]}'
            module = __import__(f'commands.{module_name}', fromlist=['setup'])
            module.setup(TREE, MY_GUILD)
            MODULE_TREE.append(module_name)


@CLIENT.event
async def on_member_join(member):
    embed = discord.Embed(
        title=LANGUAGE_MANAGER.event_get("member_join", "embed_title").format(member.name),
        description=LANGUAGE_MANAGER.event_get("member_join", "embed_description").format(member.name,
                                                                                          member.guild.name),
        color=discord.Color.blurple()
    )
    await member.send(embed=embed)


@CLIENT.event
async def on_member_remove(member):
    print(LANGUAGE_MANAGER.event_get("member_remove", "message").format(member.name, member.guild.name))


@CLIENT.event
async def on_ready():
    try:
        if IN_DEV_MODE and MY_GUILD:
            await TREE.sync(guild=MY_GUILD)
        else:
            await TREE.sync()
    except Exception as e:
        print(e)
    print("-" * 35)
    print(LANGUAGE_MANAGER.event_get("on_ready", "bot_ready").format(CLIENT.user.name))


# Start the bot
CLIENT.run(TOKEN)
