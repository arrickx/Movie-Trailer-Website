import media
import fresh_tomatoes

titanic = media.Movie("Titanic",
					  "It's a love but sad story between a boy and a girl",
					  "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
					  "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

shawshank = media.Movie("The Shawshank Redemption",
						"It's about a man spend 12 years to escape from jail.",
						"https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
						"https://www.youtube.com/watch?v=6hB3S9bIaco")

twentyone = media.Movie("21",
						"It's the adventure story for a smart student to make money from gambling.",
						"https://upload.wikimedia.org/wikipedia/en/a/a8/21_%282008_film%29.jpg",
						"https://www.youtube.com/watch?v=7uYESECSFYY")

inception = media.Movie("Inception",
						"It's the story a group of people can go into others dream.",
						"https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
						"https://www.youtube.com/watch?v=66TuSJo4dZM")

findingdory = media.Movie("Finding Dory",
				  		  "It's the story a father finding his son, and also a daughter finding her memories.",
						  "https://upload.wikimedia.org/wikipedia/en/3/3e/Finding_Dory.jpg",
						  "https://www.youtube.com/watch?v=WP_L1I4lmFE")

lalaland = media.Movie("La La Land",
				  		  "It's a love story between a musician and a actor.",
						  "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
						  "https://www.youtube.com/watch?v=0pdqf4P9MB8")


# Add all the movies into the movies list.
movies =[lalaland,findingdory,shawshank,titanic,inception,twentyone]


# Input the list into the function.
fresh_tomatoes.open_movies_page(movies)




