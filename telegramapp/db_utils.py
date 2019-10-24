import os
import sqlite3
from contextlib import closing

from werkzeug.utils import secure_filename

from telegramapp.secrets import UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def commit(sql, task=None, get=False):
    with closing(sqlite3.connect('beers.db', check_same_thread=False)) as conn:
        with conn:
            with closing(conn.cursor()) as cur:
                if task == None:
                    data = cur.execute(sql).fetchall()
                    conn.commit()
                    return data
                if get:
                    data = cur.execute(sql, task).fetchall()
                    conn.commit()
                    return data
                else:
                    cur.execute(sql, task)
                    conn.commit()


def get_dict(sql, task):
    return [dict(name=row[0],
                 abv=row[1],
                 rarity=row[2],
                 image_file=row[3],
                 animation=row[4],
                 in_use=row[5],
                 id=row[6])
            for row in commit(sql, task, get=True)]


def get_records():
    sql = "SELECT * FROM beers"
    try:
        return get_dict(sql, task=None)
    except Exception as e:
        return e


def get_beer_by_name(name):
    try:
        sql = '''SELECT * FROM beers WHERE Name=?'''
        return get_dict(sql, (name,))
    except Exception as e:
        return e


def get_beer_by_id(id):
    sql = '''SELECT * FROM beers WHERE ID=?'''
    try:
        return get_dict(sql, (id,))
    except Exception as e:
        return e


def get_column(value):
    try:
        sql = '''SELECT {} From beers'''\
            .format(value)
        return [val[0] for val in commit(sql, task=None, get=True)]
    except Exception as e:
        return e


def update(beer, form):
    """
    use the beer for immutable data and the form for mutable data
    that will be updated
    """
    task = ()
    sql = '''
            UPDATE beers
            SET abv = ? ,
                abv_color = ? ,
                rarity = ? ,
                rarity_color = ? ,
                in_use = ?
            WHERE name = ?
            '''
    try:
        commit(sql, task)
        return "Beer updated"
    except Exception as e:
        return e


def insert(data):
    task = (data['Name'],
            data['ABV'],
            data['Rarity'],
            data['ImageFile'],
            data['Animation'],
            -1)
    sql = '''INSERT INTO beers(Name, ABV, Rarity, ImageFile, Animation, InUse) 
        VALUES(?, ?, ?, ?, ?, ?) '''
    try:
        commit(sql, task)
        return "Beer created"
    except Exception as e:
        return e

def set_tap(tap, beer_name):
    try:
        task = (tap, beer_name)
        sql = '''
            UPDATE beers
            SET in_use = ?
            WHERE name = ?
            '''
        commit(sql, task)
        return "{} set to {}".format(tap, beer_name)
    except Exception as e:
        return e