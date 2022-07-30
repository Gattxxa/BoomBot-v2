from discord import Embed
from random import choice

from .modules.common import *
from .modules.spell import spell_map, init_map_pool


# /valo map ignore:
def valo_map(ignore_text: str) -> Embed:
    maps = init_map_pool()

    # Process: Map Ban
    for text in ignore_text.split():
        map_name, _, _ = spell_map(text)
        try: maps.remove(map_name)
        except: pass

    # Success: Map Select
    if maps:
        selected = choice(maps)
        map_name, image, thumbnail = spell_map(selected)
        embed = Embed(title=MAP_TTL_SUC, color=SUCCESS)
        embed.add_field(name='Map', value=f' 🗺 {map_name}')
        embed.set_image(url=image)
        embed.set_thumbnail(url=thumbnail)
        return embed

    # Error: There are mo selectable maps.
    else:
        embed = Embed(title=MAP_TTL_ERR, color=ERROR)
        return embed
