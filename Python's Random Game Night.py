import random

def guess_item():
    items = ['book', 'laptop', 'camera', 'headphone', 'backpack']
    selected_item = random.choice(items)
    
    while True:
        guess = input('Guess which item in the list was selected: ')
        
        if guess == selected_item:
            print("Congratulations! You guessed correctly.")
            break
        else:
            print("Sorry, that's not correct. Try again.")
guess_item()