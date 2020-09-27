songs = ["ROCKSTAR", "Do It", "For The Night"]

# Print first and last elements of songs list
print(songs[0])
print(songs[2])

# Print "Do It"and "For The Night" using a list slice
print(songs[1:3])

# update the first element
songs[2] = "My Songs Know What You Did In The Dark (Light Em Up)"
print(songs)

# Add 3 more songs to the list
songs.extend(["Scream Saver", "STEREOPLEIN (Yellow Claw Remix)", "Pop/Stars & Mic Drop (ft. (G)I-DLE, Madison Beer, Jaira Burns & Steve Aoki) MASHUP"])
print(songs)

# Delete one element from list
# All my tracks are bangers so I'm only deleting the defaults.
del songs[0:3]
print(songs)

# Option 1
for song in songs:
    print(song)

# Option 2
for i in range(len(songs)):
    print(songs[i])

# Create animals list and fill with 3 animal names.
# Add one more animal
# Print the 3rd animal
# Delete the first animal
# Print all animal names using a loop

animals = ["Glaucus Atlanticus", "Venezuelan Poodle Moth", "Superb Bird of Paradise"]
print(animals)
animals.append("Axolotl")
print(animals[2])
del animals[0]
print(animals)

for animal in animals:
    print(animal)