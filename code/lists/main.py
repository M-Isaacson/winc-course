# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

"""
================
Exercise: Lists
================
"""

# Function alphabetical_order 
def alphabetical_order(my_list):
    my_list.sort()
    return my_list

#movies = ['War Horse','Superman','Empire of the Sun','Memoirs of a Geisha']
#print(alphabetical_order(movies))

# Function won_golden_globe
def won_golden_globe(movie):
    golden_globe_movies = ['jaws','superman','e.t. the extra-terrestrial','memoirs of a geisha']
    if movie.lower() in golden_globe_movies:
        return True
    else:
        return False

#print(won_golden_globe('Superman'))

# Function remove_toto_albums
def remove_toto_albums (album_list):
    toto_albums = ['Fahrenheit','The Seventh One','Toto XX','Falling in Between','35th Anniversary – Live in Poland','Toto XIV','Old Is New','40 Tours Around the Sun','With a Little Help from My Friends']
    new_album_list = album_list.copy()
    for album in album_list:
        if album in toto_albums:
            new_album_list.remove(album)
    return new_album_list

#print(remove_toto_albums(['Fahrenheit','Funfgraden','Toto XX','Whatsup','Old Is New']))
#print(remove_toto_albums(['Funfgraden','Whatsup']))
#print(remove_toto_albums(['Fahrenheit','Toto XX','Old Is New']))