from discord import app_commands
from discord.ext import commands

from commands.modules.common import *
from commands.help import valo_help
from commands.rank import valo_rank, valo_rank_update 
from commands.list import valo_list
from commands.team import valo_team
from commands.map import valo_map


# Global Command - /valo 
class GlobalValo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    # Make '/valo' Group
    valo = app_commands.Group(name='valo', description=DESC_VALO)


    # /valo help
    @valo.command(name='help', description=DESC_HELP)
    async def slash_valo_help(self, ctx):
        embed = valo_help()
        await ctx.response.send_message(embed=embed)


    # /valo rank update:
    @valo.command(name='rank', description=DESC_RANK)
    @app_commands.describe(update=DESC_RANK_ARG)
    async def slash_valo_rank(self, ctx, update:str=None):
        if update:
            embed = valo_rank_update(ctx.user, update)
        else:
            embed = valo_rank(ctx.user)   
        await ctx.response.send_message(embed=embed)
            

    # /valo list
    @valo.command(name='list', description=DESC_LIST)
    async def slash_valo_list(self, ctx):
        embeds = valo_list(ctx)
        await ctx.response.send_message(embeds=embeds)
        

    # /valo team ignore:
    @valo.command(name='team', description=DESC_TEAM)
    @app_commands.describe(ignore=DESC_TEAM_ARG)
    async def slash_valo_team(self, ctx, ignore:str='None'):
        embeds = valo_team(ctx, ignore, False)
        if len(embeds) > 1:
            await ctx.response.send_message(embeds=embeds)
        else:
            await ctx.response.send_message(embed=embeds[0])
    

    # /valo random ignore:
    @valo.command(name='random', description=DESC_RANDOM)
    @app_commands.describe(ignore=DESC_RANDOM_ARG)
    async def slash_valo_random(self, ctx, ignore:str='None'):
        embeds = valo_team(ctx, ignore, True)
        if len(embeds) > 1:
            await ctx.response.send_message(embeds=embeds)
        else:
            await ctx.response.send_message(embed=embeds[0])
    

    # /valo map ignore:
    @valo.command(name='map', description=DESC_MAP)
    @app_commands.describe(ignore=DESC_MAP_ARG)
    async def slash_valo_map(self, ctx, ignore:str='None'):
        embed = valo_map(ignore)
        await ctx.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(GlobalValo(bot))
