from sys import argv

def average(numbers):
    '''Returns the average of the list numbers.'''
    numbers_list=list(numbers)
    sum=0
    for num in numbers_list:
        sum+=int(num)
        average_number = sum / len(numbers_list)
    return f"The average of {numbers_list} is {average_number}"

def main():
    print(average(argv[1:]))


if __name__ == "__main__":
    main()

