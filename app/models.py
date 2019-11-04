from flask import request
from sqlalchemy import MetaData, create_engine, Table, Column, select, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import pandas as pd


metadata = MetaData()
engine = create_engine('sqlite:///beers.db', connect_args={'check_same_thread': False}, echo=False)  # echo=False
Base = declarative_base()
db_session = sessionmaker(bind=engine)()


class Beer(Base):
    __tablename__ = 'beers'

    name = Column(String(64), primary_key=True, nullable=False)
    val1 = Column(Integer, nullable=False)
    val2 = Column(Integer, nullable=False)
    val3 = Column(Integer, nullable=False)
    val4 = Column(Integer, nullable=False)
    val5 = Column(Integer, nullable=False)
    rarity = Column(Integer, nullable=False)
    abv = Column(Integer, nullable=False)
    pattern = Column(Integer, nullable=False)
    tap = Column(Integer, nullable=False)

    def __rep__(self):
        return '<BEER {}>'.format(self.name)


def delete_beer(beer):
    db_session.query(Beer).filter_by(name=beer.name).delete()
    db_session.commit()


def get_records():
    return pd.read_sql_table('beers', engine)


def get_beer_by_name(beername):
    beer = db_session.query(Beer).filter_by(name=beername).first()
    return beer


def get_names():
    beers = db_session.query(Beer).all()
    return [beer.name for beer in beers]


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
        db_session.add(beer)
        db_session.commit()
        return "Beer created"
    except Exception as e:
        return e


def update_tap(beername, tap_number):
    old_beer = db_session.query(Beer).filter_by(tap=tap_number).first()
    if old_beer != None:
        old_beer.tap = -1
    new_beer = db_session.query(Beer).filter_by(name=beername).first()
    new_beer.tap = tap_number
    db_session.commit()


'''
def set_tap(tap, beer_name):
    try:
        task = (tap, beer_name)
        sql = ''''''
            UPDATE beers
            SET tap = ?
            WHERE name = ?
            ''''''
        commit(sql, task)
        return "tap {} set to {}".format(tap, beer_name)
    except Exception as e:
        return e
'''