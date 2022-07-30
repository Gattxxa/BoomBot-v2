import sqlite3
import json

DATABASE = './tools/BoomBot.db'


# Create
def create():
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute('CREATE TABLE users(id integer PRIMARY KEY, rank text, last_updated text);')
    con.commit()
    cur.close()
    con.close()


# Insert
# [(id, rank, last_updated), (id, rank, last_updated), (id, rank, last_updated)]
def insert(users:list):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    for user in users:
        id, rank, last_updated = user
        try:
            cur.execute(f'INSERT INTO users(id, rank, last_updated) values({id}, "{rank}", "{last_updated}");')
        except:
            pass
    con.commit()
    cur.close()
    con.close()


# Update
# [(id, rank, last_updated), (id, rank, last_updated), (id, rank, last_updated)]
def update(users:list):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    for user in users:
        id, rank, last_updated = user
        try:
            cur.execute(f'UPDATE users SET rank = "{rank}", last_updated = "{last_updated}" WHERE id = {id};')
        except:
            pass
    con.commit()
    cur.close()
    con.close()


# Delete
# [id, id, id]
def delete(ids:list=[]):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    if len(ids) > 1:
        cur.execute(f'DELETE FROM users WHERE id IN {tuple(ids)};')
    elif len(ids) == 1:
        cur.execute(f'DELETE FROM users WHERE id = {ids[0]};')
    else:
        pass
    con.commit()
    cur.close()
    con.close()


# Select
# [id, id, id]
def select(ids: list=[]):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    if len(ids) > 1:
        cur.execute(f'SELECT * FROM users WHERE id IN {tuple(ids)};')
    elif len(ids) == 1:
        cur.execute(f'SELECT * FROM users WHERE id = {ids[0]};')
    else:
        cur.execute('SELECT * FROM users;')
    result = cur.fetchall()
    cur.close()
    con.close()
    return result


# Select Rank
def select_rank(ranks: list=[]):
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    if len(ranks) > 1:
        cur.execute(f'SELECT * FROM users WHERE rank IN {tuple(ranks)};')
    elif len(ranks) == 1:
        cur.execute(f'SELECT * FROM users WHERE rank = {ranks[0]};')
    else:
        cur.execute('SELECT * FROM users;')
    result = cur.fetchall()
    cur.close()
    con.close()
    return result


# Import from .json
def import_by_json(file):
    result = []
    with open(f'./tools/import/{file}.json', encoding='utf-8') as f:
        users = json.load(f)
    for user_id in users:
        id = int(user_id)
        rank = str(users[user_id]['rank'])
        last_updated = str(users[user_id]['last_updated'])
        result.append((id, rank, last_updated))
    return result
