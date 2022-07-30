from discord import app_commands, Object
from discord.ext import commands

from env import HOME

from commands.modules.common import *
from commands.statistics import valo_statistics


# Guild Command - /valo 
class GuildValo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    # Make '/valo' Group
    valo = app_commands.Group(name='valo', description=DESC_VALO)


    # /valo statistics
    @valo.command(name='statistics', description='統計情報の表示')
    async def slash_valo_statistics(self, ctx):
        embeds = valo_statistics()
        await ctx.response.send_message(embeds=embeds)


async def setup(bot):
    await bot.add_cog(GuildValo(bot), guilds=[Object(id=HOME),])
