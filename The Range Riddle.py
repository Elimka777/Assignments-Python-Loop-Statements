#Task 1: Your Mood Today
days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
moods = ["happy", "sad", "energetic", "calm", "peaceful", "creative", "curious"]
#Using the range() function, loop through the days of the week and for each day, randomly select a mood from the list and print it. 
import random
for day in range(len(days_of_the_week)):
    mood = random.randint(0,len(moods)-1)
    print(f"On {days_of_the_week[day]} you were feeling {moods[mood]}.")
