genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

# Creating a sublist of genres from the second to the fourth track
sublist = genres[1:4]

# Looping through the sublist and printing out the genres
for genre in sublist:
    print(genre)
genres_with_music = [genre + " Music" for genre in genres]

# Printing the new list
print(genres_with_music)

for i in range(10, 0, -1):
    print(i)
print("The beat drops now!")