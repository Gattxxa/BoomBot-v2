from discord import Embed
import itertools
from random import randint

from .modules.common import *
from .modules.player import get_players, get_participants, sum_points

# /valo team ignore:
def valo_team(ctx, ignore_text: str, random: bool):

    # Error: Not in a voice channel.
    try:
        channel = ctx.user.voice.channel
        players = get_players(channel)
    except AttributeError:
        embed = Embed(title=LIST_TTL_ERR, color=ERROR)
        return [embed]

    # Warning: If one member of the voice channel is able to get.
    if players:
        participants = get_participants(players, ignore_text)
    else:
        embed = Embed(title=LIST_TTL_WAR, color=WARNING)
        embed.set_footer(text=LIST_FOOT_WAR)
        return [embed]
    
    # Process: When the appropriate number of participants.
    if participants:
        r = int(len(participants)//2)
        teams = list(itertools.combinations(participants, r))
        teams_point = [sum_points(team) for team in teams]
    else:
        num, value = len(players), ''
        title = f'参加者の数が不正です　({num}/10人)'
        for i in range(num):
            player = players[i]
            value += f'{i} - {player.emoji}<@{player.id}>\n'
        embed = Embed(title=title, color=ERROR)
        embed.add_field(name='IgnoreID', value=value, inline=True)
        embed.set_footer(text=LIST_FOOT_SUC)
        return [embed]

    # ProcessBranch: Completely random / War power reference
    if random:
        i = randint(0, len(teams)-1)
        j = -1*(i+1)
        atk_team, def_team = teams[i], teams[j]
        oth_desc=''
    else:
        now_diff = 20210801
        for i in range(len(teams)):
            j = -1*(i+1)
            diff = abs(teams_point[i]-teams_point[j])
            if diff < now_diff:
                now_diff = diff
                picklist = [(teams[i], teams[j])]
            elif diff == now_diff:
                picklist.append((teams[i], teams[j]))
            else:
                continue
        half = int(len(picklist)//2)
        pick = randint(1, half)
        if randint(0, 1):
            atk_team, def_team = picklist[pick-1]
        else:
            atk_team, def_team = picklist[pick*-1]
        oth_desc=f'チーム戦力の差：{now_diff}\n組み合わせ候補：{pick}/{half}'

    # Process: Show Team member
    atk_desc, def_desc = '', ''
    for i in range(r):
        ap, dp = atk_team[i], def_team[i]
        if ap.id != -1:
            atk_desc += f'{ap.emoji}<@{ap.id}>\n'
        if dp.id != -1:
            def_desc += f'{dp.emoji}<@{dp.id}>\n'
    
    # Success:
    atk_embed = Embed(title='Attacker Side', description=atk_desc, color=ATTACKER)
    def_embed = Embed(title='Defender Side', description=def_desc, color=DEFENDER)
    other_embed = Embed(title='Information', description=oth_desc, color=OTHER)
    if random:
        return [atk_embed, def_embed]
    else:
        return [atk_embed, def_embed, other_embed]
