def eligible_for_senate(a,b):
    if a>=30 and b>=9:
        return("yes")
    else:
        return("no")
    pass

def eligible_for_house(i,j):
    if i>=25 and j>=7:
        return("yes")
    else:
        return("no")
    pass

def main():
    print("\nCONGRESS ELIGIBILITY\n")
    age=int(input("Enter age of candidate: "))
    length_of_citizenship=int(input("Enter years of U.S. citizenship: "))
    if eligible_for_house(age,length_of_citizenship)=="yes":
        if eligible_for_senate(age,length_of_citizenship)=="yes":
            print("\nThe candidate is eligible for election to the House of Representatives and the Senate.\n")
        else:
            print("\nThe candidate is eligible for election to the House of Representatives but is NOT eligible for election to the Senate.\n")
    else:
        print("\nThe candidate is NOT eligible for election to either the House of Representatives or the Senate.\n")
    pass

if __name__ == "__main__":
    main()
