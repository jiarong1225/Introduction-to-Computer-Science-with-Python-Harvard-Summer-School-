def sign(month, day):
    sum_dates=0
    for n in range (1,month+1):
        if n<month:
            if n!=2:
                month_dates=n%1+30
            else:
                month_dates=29
            sum_dates+=month_dates
        else:
            sum_dates+=day
    return(sum_dates)



def main():
    month=int(input("What's the month of your birthday? "))
    day=int(input("What's the date of your birthday? "))
    if (month < 1 or month > 12) or (day > month % 1+30) or (month != 2 and day > month%2+30) or (month==2 and day>29) or (day<0):
        print("INVALID_DATE")
    elif sign(3,21)<=sign(month,day)<=sign(4,19):
        print("Aries")
    elif sign(4,20)<=sign(month,day)<=sign(5,20):
        print("Taurus")
    elif sign(5,21)<=sign(month,day)<=sign(6,20):
        print("Gemini")
    elif sign(6,21)<=sign(month,day)<=sign(7,22):
        print("Cancer")
    elif sign(7,23)<=sign(month,day)<=sign(8,22):
        print("Leo")
    elif sign(8,23)<=sign(month,day)<=sign(9,22):
        print("Virgo")
    elif sign(9,23)<=sign(month,day)<=sign(10,22):
        print("Libra")
    elif sign(10,23)<=sign(month,day)<=sign(11,21):
        print("scorpio")
    elif sign(11,23)<=sign(month,day)<=sign(12,21):
        print("Sagittarius")
    elif sign(12,22)<=sign(month,day)<=sign(12,31) or sign(month,day)<=sign(1,19):
        print("Capricorn")
    elif sign(1,20)<=sign(month,day)<=sign(2,18):
        print("Aquarius")
    elif sign(2,19)<=sign(month,day)<=sign(3,20):
        print("Pisces")



if __name__ == "__main__":
    main()
