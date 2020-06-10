print("Check out this amazing Top 250 high rated Movies of all the time:\n")

import imdb
ia=imdb.IMDb()
search=ia.get_top250_movies()
count=1
for i in range(250):
    print(f"{count}. {search[i]}")
    count+=1
