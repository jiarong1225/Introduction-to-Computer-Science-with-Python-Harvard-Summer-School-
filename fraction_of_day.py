def fraction_of_day(x,y,z,h):
    total_seconds=24*3600
    total_seconds=24*3600
    if (h=='A' and x==12):
        sum_seconds=y*60+z
    elif (h=='A' and x!=12):
        sum_seconds= x*3600
    elif (h=='P' and x==12):
        sum_seconds=12*3600+y*60+z
    elif (h=='P' and x!=12):
        sum_seconds=12*3600+x*3600+y*60+z
    formatted_number = f"{sum_seconds/total_seconds:.04f}"
    return(formatted_number)


def main():
    print(f"{"Time":>10}",end="\t")
    print(f"{"Fractions since midnight":<25}")
    print(f"{"12:00 AM":>10}",end="\t")
    print(f"{fraction_of_day(12,0,0,'A'):<25}")
    for i in range(1,12):
        print(f"{i:>4}", end=":00 AM\t")
        print(f"{fraction_of_day(i,0,0,'A'):<25}")
    print(f"{"12:00 PM":>10}",end="\t")
    print(f"{fraction_of_day(12,0,0,'P'):<25}")
    for i in range(1,12):
        print(f"{i:>4}",end=":00 PM\t")
        print(f"{fraction_of_day(i,0,0,'P'):<25}")


if __name__ == "__main__":
    main()
