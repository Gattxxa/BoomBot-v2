from discord import Intents, Object, Game
from discord.ext import commands

from env import TOKEN, HOME

# Implementation
class BoomBot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(command_prefix='/', intents=Intents.default())

    async def setup_hook(self):

        # Global Slash Commands
        GLOBAL_EXTENSION_COGS_ = ['cogs.global.slash_valo']
        for gec in GLOBAL_EXTENSION_COGS_:
            await self.load_extension(gec)
        await bot.tree.sync(guild=None)

        # Guild Slash Commands
        GUILD_EXTENSION_COGS_ = ['cogs.guild.slash_valo']
        for gec in GUILD_EXTENSION_COGS_:
            await self.load_extension(gec)
        await bot.tree.sync(guild=Object(id=HOME))

    async def on_ready(self):
        await self.change_presence(activity=Game(name="Valorant Season 6に対応しました。"))


if __name__ == '__main__':
    bot = BoomBot()
    bot.run(TOKEN)
