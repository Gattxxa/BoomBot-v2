from discord import Embed

import tools.database as db

from .modules.common import *


# /valo statistics
def valo_statistics() -> Embed:
    users = f'{len(db.select_rank([]))}人'
    users_total = Embed(title='利用者数合計', description=users)

    iron = f"{len(db.select_rank(['アイアン１', 'アイアン２', 'アイアン３']))}人"
    bronze = f"{len(db.select_rank(['ブロンズ１', 'ブロンズ２', 'ブロンズ３']))}人"
    silver = f"{len(db.select_rank(['シルバー１', 'シルバー２', 'シルバー３']))}人"
    gold = f"{len(db.select_rank(['ゴールド１', 'ゴールド２', 'ゴールド３']))}人"
    platinum = f"{len(db.select_rank(['プラチナ１', 'プラチナ２', 'プラチナ３']))}人"
    diamond = f"{len(db.select_rank(['ダイヤモンド１', 'ダイヤモンド２', 'ダイヤモンド３']))}人"
    ascendant = f"{len(db.select_rank(['アセンダント１', 'アセンダント２', 'アセンダント３']))}人"
    immortal = f"{len(db.select_rank(['イモータル１', 'イモータル２', 'イモータル３']))}人"
    radiant = f"""{len(db.select_rank(['"レディアント"']))}人"""
    norank = f"""{len(db.select_rank(['"ランクなし"']))}人"""
    ranks_total = Embed(title='ランク別利用者数')
    ranks_total.add_field(name='アイアン', value=iron, inline=False)
    ranks_total.add_field(name='ブロンズ', value=bronze, inline=False)
    ranks_total.add_field(name='シルバー', value=silver, inline=False)
    ranks_total.add_field(name='ゴールド', value=gold, inline=False)
    ranks_total.add_field(name='プラチナ', value=platinum, inline=False)
    ranks_total.add_field(name='ダイヤモンド', value=diamond, inline=False)
    ranks_total.add_field(name='アセンダント', value=ascendant, inline=False)
    ranks_total.add_field(name='イモータル', value=immortal, inline=False)
    ranks_total.add_field(name='レディアント', value=radiant, inline=False)
    ranks_total.add_field(name='ランクなし', value=norank, inline=False)

    return [users_total, ranks_total]
