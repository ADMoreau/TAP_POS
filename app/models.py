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
    
    ID   = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(64), nullable=False)
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


def get_beer_by_tap(tapno):
    try:
        beer = db_session.query(Beer).filter_by(tap=tapno).first()
        return beer
    except Exception as e:
        return e


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
    return list(set([beer.name for beer in beers]))


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
        beer.abv = str(request.form['abv1']) + str(request.form['abv2']) + str(request.form['abv3'])
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
    temp_beer = Beer()
    temp_beer.val1 = new_beer.val1
    temp_beer.val2 = new_beer.val2
    temp_beer.val3 = new_beer.val3
    temp_beer.val4 = new_beer.val4
    temp_beer.val5 = new_beer.val5
    temp_beer.name = new_beer.name
    temp_beer.rarity = new_beer.rarity
    temp_beer.abv = new_beer.abv
    temp_beer.pattern = new_beer.pattern
    temp_beer.tap = tap_number
    db_session.add(temp_beer)
    db_session.commit()
