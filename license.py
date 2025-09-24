from random import randint


def random_capital():
    return(chr(randint(65,90)))


def random_plate():
    capitals=[]
    for i in range(3):
        capitals.append(random_capital())
    digits = 100 * randint(1, 9) + 10 * randint(0, 9) + randint(0, 9)
    plate_str = str(digits) + " " + ''.join(capitals)
    return(plate_str)


def main():
    for n in range(20):
        print(random_plate())


if __name__ == "__main__":
    main()
