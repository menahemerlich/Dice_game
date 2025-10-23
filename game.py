import random

def roll_two_d6():
    roll_1 = random.randint(1, 6)
    roll_2 = random.randint(1, 6)
    return roll_1, roll_2


def is_bust(score: int):
    if score >= 100:
        return True
    return False

def is_exact_100(score: int):
    if score == 100:
        return True
    return False

def closer_to_target(a: int, b: int, target: int = 100):
    if (target - a) < (target - b):
        return 1
    elif (target - b) < (target - a):
        return 2
    else:
        return None

def tie_breaker():
    p1 = 0
    p2 = 0
    while p1 == p2:
        p1 = sum(roll_two_d6())
        p2 = sum(roll_two_d6())

        if p1 > p2:
            return 1
        else:
            return 2

def turn_decision():
    choice = ''
    options = ["r", "p"]
    while choice not in options:
        choice = input("Enter your choice: ")
    return choice

def play_game():
    while score1 < 100
        choice = turn_decision()
        if choice == "r":
            p1 = roll_two_d6()

