import discord
from discord_logger import DiscordLogger

logger = DiscordLogger().get_logger()


class DiscordBot:
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        self.client = discord.Client(intents=intents)

        @self.client.event
        async def on_ready():
            print(f'We have logged in as {self.client.user}')
            logger.info(f'We have logged in as {self.client.user}')

        @self.client.event
        async def on_message(message):
            if message.author == self.client.user:
                return

            if message.content.startswith('$hello'):
                await message.channel.send('Hello!')
                logger.info(f'Hello message sent to {message.channel}')
            else:
                await message.channel.send('Whut??')
                logger.info(f'Unknown message sent to {message.channel}')

    def run(self):
        with open("assets/token.txt", "r") as f:
            token = f.read().strip()

        self.client.run(token, log_handler=None)


if __name__ == "__main__":
    print("Starting bot...")

    bot = DiscordBot()
    bot.run()
