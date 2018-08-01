# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes
ghost_rider=media.Movie("GHOST RIDER","SUPERNATURAL SUPERHERO","https://upload.wikimedia.org/wikipedia/en/thumb/7/71/GhostRiderBigPoster.jpg/220px-GhostRiderBigPoster.jpg","https://www.youtube.com/watch?v=tp12CD2A4NA")
#print (toy_story.storyline)
avatar=media.Movie("AVATAR","A MARINE ON AN ALIEN PLANET","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://youtu.be/5PSNL1qE6VY")
#print (avatar.storyline)
#avatar.show_trailer()
john_wick=media.Movie("JOHN WICK","Crime film/Thriller", "https://upload.wikimedia.org/wikipedia/en/thumb/9/98/John_Wick_TeaserPoster.jpg/220px-John_Wick_TeaserPoster.jpg","https://www.youtube.com/watch?v=C0BMx-qxsP4")
the_dark_night=media.Movie("THE DARK NIGHT","Drama/Crime Film","https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg","https://www.youtube.com/watch?v=EXeTwQWrcwY")
dead_pool=media.Movie("DEADPOOL","Fantasy/Science fiction film","https://upload.wikimedia.org/wikipedia/en/thumb/4/46/Deadpool_poster.jpg/220px-Deadpool_poster.jpg","https://www.youtube.com/watch?v=gtTfd6tISfw")
dead_pool2=media.Movie("DEADPOOL 2","Fantasy/Science fiction film","https://upload.wikimedia.org/wikipedia/en/c/cf/Deadpool_2_poster.jpg","https://www.youtube.com/watch?v=20bpjtCbCz0")
movies = [ghost_rider, the_dark_night, avatar, john_wick, dead_pool,dead_pool2]
fresh_tomatoes.open_movies_page(movies)
