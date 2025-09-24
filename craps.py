import random

def craps():
    point = get_point()
    if play_from_point(point)==True:
        print("YOU WIN")
    elif play_from_point(point)==False:
        print("YOU LOSE")



def print_roll(roll1, roll2):
    print(f"Computer rolls a {roll1} and a {roll2}, for a total of {roll1 + roll2}.")

def do_roll():
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    print_roll(roll1, roll2)
    return roll1 + roll2

def get_point():
    point = 0
    while point not in [4, 5, 6, 8, 9, 10]:
        point = do_roll()
    print(f"{point} is now the established POINT.")
    return point

def play_from_point(point):
    sum_ = 0
    while sum_!= point:
        sum_ = do_roll()
        if sum_ == 7:
            return False
    return True

def main():
    craps()

if __name__ == "__main__":
    main()
