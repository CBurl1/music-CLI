#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///playlist.db')
    Session = sessionmaker(bind=engine)
    session = Session()

session.query(Stream).delete()
session.query(Listener).delete()
session.query(Song).delete()
session.commit()

s1 = Song(name='Ladders', artist="Mac Miller", year=2018)
s2 = Song(name='Für Elise', artist="Ludwig van Beethoven", year=1810)

l1 = Listener(name="Jesse", age= 30)
l2 = Listener(name="Andre", age= 27)
l3 = Listener(name="Tom", age= 28)
l4 = Listener(name="Collin", age= 23)

st1 = Stream(song_name=s1.name, song=s1, listener= l4)
st2 = Stream(song_name=s2.name, song=s2, listener=l3)

session.add_all([s1, s2, l1, l2, l3,l4, st1, st2])
session.commit()