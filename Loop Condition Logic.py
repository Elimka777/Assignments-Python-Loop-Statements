scoop = 0
condition_met = False

while not condition_met:
    print("Can I get more?")
    scoop += 1
    if scoop >= 5: # Update the condition when the counter reaches 5
        condition_met = True