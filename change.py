def find_change():
    d2_price=int(input("What is the stock prices on day 1: "))
    change_utmost=0
    for i in range(2,11):
        d1_price=d2_price
        d2_price=int(input("What is the stock prices on the next day: "))
        change=abs(d2_price-d1_price)
        if change>change_utmost:
            change_utmost=change
            day1_num=i-1
            day1_price=d1_price
            day2_price=d2_price
    print_change(day1_price, day2_price, day1_num)



def print_change(day1_price, day2_price, day1_num):
    print("Largest change of ", abs(day1_price-day2_price) ," from ", day1_price ," to ", day2_price)
    print("occurred between day #",end="")
    print(day1_num," and day #",end="")
    print(day1_num+1,end=".")



def main():
    find_change()


if __name__ == "__main__":
    main()
