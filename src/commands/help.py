from discord import Embed

from .modules.common import *


# /valo help
def valo_help() -> Embed:
    embed = Embed(title=VERSION, color=BOOMBOT)
    embed.add_field(name='公式WEBページ', value=OFFICIA_URL, inline=False)

    return embed
