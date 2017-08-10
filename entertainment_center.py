import media
import fresh_tomatoes

"""
The following codes create new instances by use the class movie.
It saved the information to the specific catergory,such as title,
storyline, poster image url, and trailer url.
For the poster image url,I use google url shortener to
make the url shorter.
"""
titanic = media.Movie("Titanic",
                      "It's a love but sad story between a boy and a girl",
                      "https://goo.gl/rgSb3N",
                      "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

shawshank = media.Movie("The Shawshank Redemption",
                        "It's about a man spend 12 years to escape from jail.",
                        "https://goo.gl/mqccUL",
                        "https://www.youtube.com/watch?v=6hB3S9bIaco")

twentyone = media.Movie("21",
                        "It's the adventure story for a smart student\
                         to make money from gambling.",
                        "https://goo.gl/Hbbwii",
                        "https://www.youtube.com/watch?v=7uYESECSFYY")

inception = media.Movie("Inception",
                        "It's the story a group of people can go \
                        into others dream.",
                        "https://goo.gl/LQf9bf",
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")

findingdory = media.Movie("Finding Dory",
                          "It's the story a father finding his son,\
                           and also a daughter finding her memories.",
                          "https://goo.gl/cfKbHS",
                          "https://www.youtube.com/watch?v=WP_L1I4lmFE")

lalaland = media.Movie("La La Land",
                       "It's a love story between a musician and a actor.",
                       "https://goo.gl/rN4Mas",
                       "https://www.youtube.com/watch?v=0pdqf4P9MB8")


# Add all the movies into the movies list.
movies = [lalaland, findingdory, shawshank, titanic, inception, twentyone]


# Input the list into the function.
fresh_tomatoes.open_movies_page(movies)
