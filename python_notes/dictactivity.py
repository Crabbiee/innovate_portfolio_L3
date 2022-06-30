################################# ACTIVITY 1
# countries = {
#     "united kingdom":"london",
#     "france":"paris",
#     "germany":"berlin",
#     "spain":"madrid",
#     "italy":"rome"
# } # # INITIAL DICTIONARY

# countries.setdefault("sweden","stockholm")
# countries.setdefault("japan","tokyo")
# # # ADDED VALUES TO DICTIONARY

# for x in countries.items():
#     print(x)
# # # PRINT DICTIONARY

# countries.update({
#     "united kingdom":"english",
#     "france":"french",
#     "germany":"german",
#     "spain":"spanish",
#     "italy":"italian",
#     "sweden":"swedish",
#     "japan":"japanese"
# })
# # # ADDED 2 MORE ITEMS TO DICTIONARY

# for x in countries.items():
#     print(x)

# # PRINT OF FINAL LIST
##################################################

#######################################ACTIVITY 2

fav_songs = [{
    "Artist":"Green day",
    "Song name":"Basket case",
    "Genre":"Pop-punk",
    "Release year":"1994"
},
{
    "Artist":"System of a down",
    "Song name":"Deer dance",
    "Genre":"Metal",
    "Release year":"2001"
},
{
    "Artist":"Snails house",
    "Song name":"Pixel galaxy",
    "Genre":"EDM",
    "Release year":"2017"
}]

print(fav_songs)

fav_songs.append({"Artist":"Lorde",
    "Song name":"Tennis court",
    "Genre":"Pop",
    "Release year":"2013"})

print(fav_songs)