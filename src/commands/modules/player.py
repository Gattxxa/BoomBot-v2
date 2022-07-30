import discord

import tools.database as db

from .spell import spell_rank


class Player():
    def __init__(self, id: int, nick: str, rank: str, last_updated: str):
        _, emoji, point = spell_rank(rank)
        self.id = id
        self.nick = nick
        self.rank = rank
        self.last_updated = last_updated
        self.emoji = emoji
        self.point = point

    def set_pint(self, point: int):
        self.point = point


# Get players information from voice channels.
def get_players(channel: discord.VoiceChannel):
    NICK, RANK, LAST_UPDATED = 'nick', 'rank', 'last_updated'
    players, players_info = [], {}

    # When members information could not be get.
    try: members = channel.members
    except: return []
    if not members: return []
    
    # Assume everyone is a player except the bot.
    for member in members:
        if member.bot: continue
        id, nick = member.id, member.nick
        players_info[id] = {NICK:nick, RANK:'ランクなし', LAST_UPDATED:'-'}
    
    # Reflects information of players who have already registered their rank information.
    users_data = db.select(list(players_info))
    for data in users_data:
        id, rank, last_updated = data
        players_info[id][RANK] = rank
        players_info[id][LAST_UPDATED] = last_updated

    # Generate Players
    for id in list(players_info):
        nick = players_info[id][NICK]
        rank = players_info[id][RANK]
        last_updated = players_info[id][LAST_UPDATED]
        players.append(Player(id, nick, rank, last_updated))

    return players


# Participants are determined from among the players.
def get_participants(players: list, ignore_text: str):
    participants = []
    ignore = ignore_text.split()
    
    # Remove a specific player.
    for i in range(len(players)):
        if str(i) in ignore:
            continue
        participants.append(players[i])

    # Is it the right number of people?
    # 2 ≦ participants ≦ 10 and Even number.
    total = len(participants)
    if total < 2:
        return []
    if total > 10:
        return []
    if total%2 != 0:
        dummy = Player(-1, 'dummy', 'dummy', 'dummy')
        dummy.set_pint(0)
        participants.append(dummy)

    return participants


# Sum the points of the players in the list.
def sum_points(players: list) -> int:
    total = 0
    for player in players:
        total += player.point
    return total
