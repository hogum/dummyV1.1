from datetime import date

from actor import Actor
from base import Session, engine, Base
from contact_details import ContactDetails
from movie import Movie
from stuntman import Stuntman


# Generate database schema
Base.metadata.create_all(engine)


# Create new sesssion
session = Session()


# Create movies

born_funny = Movie("Born Looking Funny", date(200, 12, 2))
catchy = Movie("Catchy Catchy Cats", date(2012, 3, 16))
making_soda = Movie("Cooking Baking Soda", date(2003, 10, 30))


# Create actors

skim_phew = Actor("Skim Phew", date(2000, 6, 9))
stop_theft = Actor("Stop Theft", date(1999, 10, 10))
short_face = Actor("Short Face", date(2004, 2, 29))
longer_nose = Actor("Longer Nose", date(1999, 4, 20))


# Add actors to movies

born_funny.actors = [skim_phew]
catchy.actors = [short_face]
making_soda.actors = [short_face, longer_nose, stop_theft]


# Add contact details to actors

skim_contact = ContactDetails("29 29 29", "Front Street 3", skim_phew)
stop_contact = ContactDetails("42 40 65 44", "Cool Desert 96", stop_theft)
short_contact = ContactDetails("47 85 03 64", "Empty Waters 32", short_face)
longer_contact = ContactDetails("84 43 58 00", "Empty Waters 32", longer_nose)
stop_contact1 = ContactDetails("92 84 83 54", "Hidden Houses 54", stop_theft)


# Create stuntman

skim_stunt = Stuntman("Jumping Tree", True, skim_phew)
stop_stunt = Stuntman("Fallen Roof", True, stop_theft)
long_stunt = Stuntman("Biscuit Man", True, longer_nose)
short_stunt = Stuntman("Walking Slipper", True, short_face)


# Persist data

session.add(born_funny)
session.add(catchy)
session.add(making_soda)

session.add(skim_contact)
session.add(stop_contact)
session.add(stop_contact1)
session.add(longer_contact)
session.add(short_contact)

session.add(skim_stunt)
session.add(stop_stunt)
session.add(long_stunt)
session.add(stop_stunt)

session.commit()
session.close()
