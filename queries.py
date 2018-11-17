from actor import Actor
from base import Session
from contact_details import ContactDetails
from movie import Movie


# Extract a session

session = Session()


# Extract all movies

movies = session.query(Movie).all()

print("\n\t All Movies", "." * 5)
print('{:15}{:>25}'.format("Movie", "Release Date"))
for movie in movies:
    print('{0.title:30} {0.release_date}'.format(movie))

print('\n\n{:^20}\n'.format('Appearances'))
short_face_movies = session.query(Movie).join(
    Actor, Movie.actors).filter(
    Actor.name == "Stop Theft").all()

for movie in short_face_movies:
    print(f"Short Face appeared in {movie.title}")
    print('')


empty_contacts = session.query(Actor) \
    .join(ContactDetails) \
    .filter(ContactDetails.address.ilike('%mpty%')) \
    .all()

print("\n\tLivers of empty?\n")
for that in empty_contacts:
    print("{} is stationed in Empty Waters".format(that.name))
print('')
