def factor_class(num):
    sum=0
    for i in range(1,num-1):
        if num%i==0:
            sum+=i
    if sum<num:
        return "deficient"
    elif sum==num:
        return "perfect"
    elif sum>num:
        return "abundant"
    pass


def divisors(start, end):
    for j in range(start,end+1):
        print(j,"is",factor_class(j))
    pass


def main():
    divisors(5, 8)


if __name__ == "__main__":
    main()
