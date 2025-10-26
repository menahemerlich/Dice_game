import random
choice_two = []
score_p1 = 0
score_p2 = 0
p1 = score_p1
p2 = score_p2

def roll_two_d6():
    roll_1 = random.randint(1, 6)
    roll_2 = random.randint(1, 6)
    sum_roll = roll_1 + roll_2
    print(f"roll_1 = {roll_1}, roll_2 = {roll_2}")
    print(f"sum_roll = {sum_roll}")
    return sum_roll


def is_bust(score_p1, score_p2):
        if score_p1 < 100 and score_p2 < 100:
            return True
        else:
            if score_p1 > 100:
                print("p2 is the winner!!")
            else:
                print("p1 is the winner!!")
            return False

def two_pass(score_p1, score_p2):
    global p1
    global p2
    if (100 - score_p1) < (100 - score_p2):
        print("p1 is the winner!!")
    elif (score_p2 - 100) < (score_p1 - 100):
        print("p2 is the winner!!")
    else:
        while p1 == p2:
            p1 = roll_two_d6()
            print(f"sum_roll_p1 = {p1}")
            p2 = roll_two_d6()
            print(f"sum_roll_p2 = {p2}")
            if p1 > p2:
                print("p1 is the winner!!")
                break
            elif p2 > p1:
                print("p2 is the winner!!")
                break
            else:
                two_pass(p1, p2)


def turn_decision():
    choice = ""
    options = ["r", "p"]
    while choice not in options and choices_two(choice):
        choice = input("Enter your choice ('r' or 'p'): ")
    return choice


def choices_two(choice):
    global choice_two
    if choice == "p":
        if choice in choice_two:
            two_pass(score_p1, score_p2)
            return False
        else:
            choice_two.append(choice)
    return True


def play_game():
    global score_p1
    global score_p2
    choice_p1 = ""
    choice_p2 = ""
    while is_bust(score_p1, score_p2) and choices_two(choice_p1 or choice_p2):
        print("Player 1's turn")
        choice_p1 = turn_decision()
        if choices_two(choice_p1):
            if choice_p1 == "r":
                score_p1 += roll_two_d6()
                print(f'score_p1 is: {score_p1}')
                if is_bust(score_p1, score_p2):
                    print("Player 2's turn2")
                    choice_p2 = turn_decision()
                    if choices_two(choice_p2):
                        if choice_p2 == "r":
                            score_p2 += roll_two_d6()
                            print(f'score_p2 is: {score_p2}')
                        else:
                            continue
            else:
                if is_bust(score_p1, score_p2):
                    print("Player 2's turn")
                    choice_p2 = turn_decision()
                    if choices_two(choice_p2):
                        if choice_p2 == "r":
                            score_p2 += roll_two_d6()
                            print(f'score_p2 is: {score_p2}')
                        else:
                            continue




