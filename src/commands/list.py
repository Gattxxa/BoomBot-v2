from discord import Embed

from .modules.common import *
from .modules.player import get_players


# /valo list
def valo_list(ctx):
    embeds = []

    # Error: Not in a voice channel.
    try:
        channel = ctx.user.voice.channel
        players = get_players(channel)
    except AttributeError:
        embed = Embed(title=LIST_TTL_ERR, color=ERROR)
        embeds.append(embed)
        return embeds

    # Success: List view
    if players:
        num, value = len(players), ''
        for i in range(num):
            player = players[i]
            value += f'{i} - {player.emoji}<@{player.id}>\n'
        
            if ((i+1)%10) == 0 or (i+1) == num:
                embed = Embed(title=f'メンバーの詳細情報　({num}/10)', color=SUCCESS)
                embed.add_field(name='IgnoreID', value=value)
                if (i+1) == num:
                    embed.set_footer(text=LIST_FOOT_SUC)
                embeds.append(embed)
                value = ''

        return embeds

    # Warn: After rebooting the bot.
    else:
        embed = Embed(title=LIST_TTL_WAR, color=WARNING)
        embed.set_footer(text=LIST_FOOT_WAR)
        embeds.append(embed)

        return embeds
