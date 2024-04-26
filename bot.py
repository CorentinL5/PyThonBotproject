import discord
from discord.ext import commands
from discord_logger import DiscordLogger

logger = DiscordLogger().get_logger()

intents = discord.Intents.default()
intents.message_content = True


class DiscordBot:
    def __init__(self):

        self.bot = commands.Bot(command_prefix='$', intents=intents)

        @self.bot.event
        async def on_ready():
            logger.info(f'We have logged in as {self.bot.user}')
            print(f'We have logged in as {self.bot.user}')

        @self.bot.command()
        async def foo(ctx, arg):
            await ctx.send(arg)

        @self.bot.command()
        async def ping(ctx):
            await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

    def run(self):
        with open("assets/token.txt", "r") as f:
            token = f.read().strip()

        self.bot.run(token, log_handler=None)


if __name__ == "__main__":
    print("Starting bot...")

    bot = DiscordBot()
    bot.run()
