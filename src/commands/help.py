from discord import Embed

from .modules.common import *


# /valo help
def valo_help() -> Embed:
    info = '+ サービス開始１周年を迎えました。\n+ スラッシュコマンドに対応しました。\n- 古い形式のコマンドが使用不可になりました。'

    embed = Embed(title=VERSION, color=BOOMBOT)
    embed.add_field(name='公式WEBページ', value=OFFICIA_URL, inline=False)
    embed.add_field(name='お知らせ', value=info, inline=False)

    return embed
