user_enters=int(input("I want the maximun to be: "))

def perfect_number():
    for n in range(2,user_enters):
        i=2
        sum_integer_divisor=1
        while i<n:
            if n%i==0:
                sum_integer_divisor+=i
            i+=1
        if sum_integer_divisor==n:
            print(sum_integer_divisor)

perfect_number()
