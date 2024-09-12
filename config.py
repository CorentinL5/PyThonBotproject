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

ENCRYPTION_KEY = config["encryption_key"]

COMMANDS_DIRECTORY = config["commands_directory"]

IN_DEV_MODE = config["in_dev_mode"]

ACTIVITY = config["activity"]

BOT_INVITE = config["bot_invite"]

GUILD_ID = config["guild_id"]



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
    if GUILD_ID is not None:
        DATA_MANAGER.set_server_info(GUILD_ID, "lang", 'en')
    LANGUAGE = 'en'

LANGUAGE_MANAGER = LangManager(lang='en', langs=LANGUAGES)

# Intents
intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.messages = True

CLIENT = discord.Client(intents=intents)
TREE = app_commands.CommandTree(CLIENT)
MODULE_TREE = []

if IN_DEV_MODE:
    MY_GUILD = discord.Object(id=GUILD_ID)
else:
    MY_GUILD = GUILD_ID = None

if ACTIVITY is not None:
    if ACTIVITY["status"].lower() == "offline":
        activity_status = discord.Status.offline
    elif ACTIVITY["status"].lower() == "idle":
        activity_status = discord.Status.idle
    elif ACTIVITY["status"].lower() == "dnd" or "do_not_disturb":
        activity_status = discord.Status.dnd
    elif ACTIVITY["status"].lower() == "invisible":
        activity_status = discord.Status.invisible
    else:
        activity_status = discord.Status.online

    if ACTIVITY["type"].lower() == "playing":
        activity_type = discord.ActivityType.playing
    elif ACTIVITY["type"].lower() == "streaming":
        activity_type = discord.ActivityType.streaming
    elif ACTIVITY["type"].lower() == "listening":
        activity_type = discord.ActivityType.listening
    elif ACTIVITY["type"].lower() == "watching":
        activity_type = discord.ActivityType.watching
    elif ACTIVITY["type"].lower() == "custom":
        activity_type = discord.ActivityType.custom
    else:
        activity_type = discord.ActivityType.unknown

    # discord.Game(name=ACTIVITY["name"], type=ACTIVITY["type"])

    CLIENT.activity = discord.Activity(name=ACTIVITY["name"],
                                       type=activity_type
                                       )

    CLIENT.status = activity_status


def NO_PERM_EMBED(no_perm_command):
    return discord.Embed(
        title=LANGUAGE_MANAGER.command_get("error", "no_permission_title"),
        description=LANGUAGE_MANAGER.command_get("error", "no_permission_description").format(no_perm_command),
        timestamp=discord.utils.utcnow(),
        color=discord.Color.red()
    )
