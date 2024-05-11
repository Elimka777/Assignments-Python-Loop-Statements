genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

track_number = 1
index = 0

while index < len(genres):
    genre = genres[index]
    print(f"Track {track_number}: This is {genre}.")
    track_number += 1
    if genre == 'Hip-hop':
        break
    index += 1

for index in range(len(genres)):
    genre = genres[index]
    if genre == 'Classical':
        continue
    print(f"Track {index + 1}: Light show ready for {genre}.")
    