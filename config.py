import json
import os
import discord
from discord import app_commands
from datamanager import DataManager
from langmanager import LangManager


# Load config.json
with open("assets/config.json", "r") as f:
    config = json.load(f)


# Constants from config.json
TOKEN = config["token"]

PREFIX = config["prefix"]

ENCRYPTION_KEY = config["encryption_key"]

COMMANDS_DIRECTORY = config["commands_directory"]


GUILD_ID = config["guild_id"]
MY_GUILD = discord.Object(id=GUILD_ID)


# Other constants
BOT_NAME = "BotPy"

BOT_LOGO_PATH = "assets/images/BotPy.png"
BOT_LOGO_ATTACHMENT = "attachment://BotPy.png"
BOT_LOGO = discord.File(BOT_LOGO_PATH, filename="BotPy.png")

COMMANDS_DIRECTORIES = ["./commands"]
for root, dirs, files in os.walk(COMMANDS_DIRECTORY):
    for directory in dirs:
        if directory != '__pycache__':
            COMMANDS_DIRECTORIES.append(f"{root}/{directory}")


# Create a DataManager instance
DATA_MANAGER = DataManager(ENCRYPTION_KEY)


# Gestion of languages
LANGUAGES = [i.replace('.json', '') for i in os.listdir("languages") if i.endswith('.json')]

LANGUAGE = DATA_MANAGER.get_server_info(GUILD_ID, "lang")
if LANGUAGE is None:
    DATA_MANAGER.set_server_info(GUILD_ID, "lang", 'en')
    LANGUAGE = 'en'
print(LANGUAGE)

LANGUAGE_MANAGER = LangManager(lang=LANGUAGE, langs=LANGUAGES)


# Intents
intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.messages = True

CLIENT = discord.Client(intents=intents)
TREE = app_commands.CommandTree(CLIENT)
