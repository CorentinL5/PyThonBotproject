import os
import discord
from discord import app_commands
from config import LANGUAGE_MANAGER, TOKEN, MY_GUILD, COMMANDS_DIRECTORIES, COMMANDS_DIRECTORY

# Intents
intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

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
            module.setup(tree, MY_GUILD)


@client.event
async def on_member_join(member):
    embed = discord.Embed(
        title=LANGUAGE_MANAGER.event_get("member_join", "embed_title").format(member.name),
        description=LANGUAGE_MANAGER.event_get("member_join", "embed_description").format(member.name,
                                                                                          member.guild.name),
        color=discord.Color.blurple()
    )
    await member.send(embed=embed)


@client.event
async def on_member_remove(member):
    print(LANGUAGE_MANAGER.event_get("member_remove", "message").format(member.name, member.guild.name))


@client.event
async def on_ready():
    await tree.sync(guild=MY_GUILD)
    print(LANGUAGE_MANAGER.event_get("on_ready", "message").format(client.user.name))


# Start the bot
client.run(TOKEN)
