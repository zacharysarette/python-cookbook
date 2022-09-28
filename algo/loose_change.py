import math

def loose_change(cents):
    cents = math.floor(cents) if cents >= 1 else 0
    return {
        'Quarters': cents // 25,
        'Dimes': cents % 25 // 10,
        'Nickels': cents % 25 % 10 // 5,
        'Pennies': cents % 25 % 10 % 5
    }
