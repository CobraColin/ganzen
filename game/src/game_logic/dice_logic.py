import random

def throw(number_of_dice:int,dice_sides:int = 6) -> int:
    throwed_number = 0
    for _ in range(0,number_of_dice):
        throwed_number += random.randint(1,dice_sides)
    
    return throwed_number


