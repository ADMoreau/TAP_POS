import sqlite3
from contextlib import closing
from flask import request
from werkzeug.utils import secure_filename
import os
import time
from . import db


class Beer(db.Model):
    __tablename__ = 'beers'
    
    name = db.Column(db.String(64), primary_key=True, nullable=False)
    val1 = db.Column(db.Integer, nullable=False)
    val2 = db.Column(db.Integer, nullable=False)
    val3 = db.Column(db.Integer, nullable=False)
    val4 = db.Column(db.Integer, nullable=False)
    val5 = db.Column(db.Integer, nullable=False)
    rarity = db.Column(db.Integer, nullable=False)
    abv = db.Column(db.Integer, nullable=False)
    pattern = db.Column(db.Integer, nullable=False)
    tap = db.Column(db.Integer, nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        db.session.close()

    def __rep__(self):
        return '<BEER {}>'.format(self.name)


def get_records():
    return db.query(Beer).all()


def get_beer_by_name(beername):
    beer = db.query(Beer).filter_by(name=beername).first()
    return beer


def get_names():
    db.session.commit()
    beers = db.session.query(Beer).all()
    return [beer.name for beer in beers]
    

def update(beer, form):
    """
    use the beer for immutable data and the form for mutable data
    that will be updated

    param form : wtfforms BeerForm in app/forms.py
    """
    task = (int(request.form['val1']),
            int(request.form['val2']),
            int(request.form['val3']),
            int(request.form['val4']),
            int(request.form['val5']),
            str(request.form['beername']),
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
    try:
        beer = Beer()
        beer.val1 = int(request.form['val1'])
        beer.val2 = int(request.form['val2'])
        beer.val3 = int(request.form['val3'])
        beer.val4 = int(request.form['val4'])
        beer.val5 = int(request.form['val5'])
        beer.name = str(request.form['beername'])
        beer.rarity = int(request.form['rarity'])
        beer.abv = int(request.form['abv'])
        beer.pattern = int(request.form['pattern'])
        beer.tap = -1
        beer.save_to_db()
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

