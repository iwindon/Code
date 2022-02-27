music = ["erasure", "depeche mode", "abba"]

print(music)
print(music[0])

places = []
denver = (39.7392, 104.9903)
la = (34.0522, 118.2437)
sf = (37.7749, 122.4194)

places.append(denver)
places.append(la)
places.append(sf)

print(places)
print(places[2])

me={"height": "6 feet, 2 inches", "fav_color": "Blue", "fav_author": "Robin Cook"}

answer = input("Type height, fav_color or fav_author:  -> ")
if answer in me:
    result = me[answer]
    print(result)
