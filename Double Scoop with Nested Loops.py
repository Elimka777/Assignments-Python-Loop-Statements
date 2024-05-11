days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
moods = ["happy", "sad", "energetic", "calm", "peaceful", "creative", "curious"]
times_of_the_day = ['morning', 'afternoon', 'evening']
#Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day
import random
for day in range(len(days_of_the_week)):
    for time in range(len(times_of_the_day)):
        mood = random.randint(0,len(moods)-1)
        print(f"On {days_of_the_week[day]} {times_of_the_day[time]} you were {moods[mood]}")