from discord import Embed, Member
from datetime import date

import tools.database as db

from .modules.common import *
from .modules.spell import spell_rank


# /valo rank
def valo_rank(user: Member):
    user_data = db.select([user.id])

    #  Success: Show User Data
    if user_data:
        _, rank, last_updated = user_data[0]
        _, emoji, _ = spell_rank(rank)
        embed = Embed(title=RANK_TTL_SUC, description=RANK_DESC_SUC, color=SUCCESS)
        embed.add_field(name='Your Rank', value=f'{emoji} {rank}')
        embed.add_field(name='Last Updated', value=f'🕓 {last_updated}')
        embed.set_thumbnail(url=user.avatar)
        return embed

    #  Error: Not Founded
    else:
        embed = Embed(title=RANK_TTL_ERR, color=ERROR)
        return embed
    

# /valo rank update:
def valo_rank_update(user: Member, update: str):
    user_data = db.select([user.id])
    new_rank, new_emoji, _ = spell_rank(update)
    today = str(date.today())

    # Process: Update/Insert User Data 
    if user_data:
        db.update([(user.id, new_rank, today)])
        _, rank, _ = user_data[0]
        old_rank, old_emoji, _ = spell_rank(rank)
        value = f'{old_emoji} {old_rank}'
        embed = Embed(title=UPDATE_TTL_SUC, color=SUCCESS)
    else:
        db.insert([(user.id, new_rank, today)])
        value = '情報なし'
        embed = Embed(title=INSERT_TTL_SUC, color=SUCCESS)

    # Success:
    embed.add_field(name='Old Rank', value=value)
    embed.add_field(name='ㅤ', value='➤')
    embed.add_field(name='New Rank', value=f'{new_emoji} {new_rank}')
    embed.set_thumbnail(url=user.avatar)
    embed.set_footer(text=UPDATE_FOOT_SUC)
    return embed


# /valo delete (un-used)
def valo_delete(user: Member):
    db.delete([user.id])
    embed = Embed(title=DELETE_TTL_SUC, color=SUCCESS)
    return embed
