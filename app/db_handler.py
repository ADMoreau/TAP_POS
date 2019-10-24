import sqlite3
from contextlib import closing
from flask import request
from werkzeug.utils import secure_filename
import os

#from app.POS import app


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
    return [dict(val1=row[0],
                 val2=row[1],
                 val3=row[2],
                 val4=row[3],
                 val5=row[4],
                 name=row[5],
                 rarity=row[6],
                 abv=row[7],
                 pattern=row[8])
            for row in commit(sql, task, get=True)]


def get_records():
    sql = "SELECT * FROM beers"
    try:
        return get_dict(sql, task=None)
    except Exception as e:
        return e


def get_beer_by_name(name):
    sql = '''SELECT * FROM beers WHERE name=?'''
    try:
        return get_dict(sql, (name,))
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
    task = (int(request.form['val1']),
            int(request.form['val2']),
            int(request.form['val3']),
            int(request.form['val4']),
            int(request.form['val5']),
            str(request.form['name']),
            int(request.form['rarity']),
            int(request.form['abv']),
            int(request.form['pattern']))
    sql = '''
            UPDATE beers
            SET val1 = ? ,
                val2 = ? ,
                val3 = ? ,
                val4 = ? ,
                val5 = ? ,
                name = ? ,
                rarity = ?,
                abv = ?,
                pattern = ?
            WHERE name = ?
            '''
    try:
        commit(sql, task)
        return "Beer updated"
    except Exception as e:
        return e


def insert(form):
    task = (int(request.form['val1']),
            int(request.form['val2']),
            int(request.form['val3']),
            int(request.form['val4']),
            int(request.form['val5']),
            str(request.form['name']),
            int(request.form['rarity']),
            int(request.form['abv']),
            int(request.form['pattern']))
    sql = '''
            INSERT INTO beers
            SET val1 = ? ,
                val2 = ? ,
                val3 = ? ,
                val4 = ? ,
                val5 = ? ,
                name = ? ,
                rarity = ?,
                abv = ?,
                pattern = ?
            WHERE name = ?
            '''
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
            SET tap = ?
            WHERE name = ?
            '''
        commit(sql, task)
        return "tap {} set to {}".format(tap, beer_name)
    except Exception as e:
        return e
