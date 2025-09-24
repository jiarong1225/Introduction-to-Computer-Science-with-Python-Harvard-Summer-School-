

def print_powers_of_2(n):
    j=1
    if n==0:
         return(j)
    else:
        for v in range (1,n+1):
            j*=2
    return(j)
    pass

def main():
    n=int(input("the utmost is 2 square to the power of: "))
    for i in range (0,n+1):
        result=print_powers_of_2(i)
        print(result,end=" ")
    pass

if __name__ == "__main__":
    main()
