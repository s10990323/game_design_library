# Dice roll Library, Lorenzo Kenon, 02/18/2021, 12:32PM, v0.1


# D4 Simulator
def roll_d4(num_roll): # num_roll is an ARGUEMENT.
    import random
    
    rolls = 0 
    while rolls <= num_roll:
        result = random.randint (1,4)
        print(f"You rolled a {result} on the d4!\n")
        rolls +=  1


