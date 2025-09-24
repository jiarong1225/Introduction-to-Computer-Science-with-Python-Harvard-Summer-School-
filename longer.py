def print_longer(list1, list2):
    '''Prints out the longer list as well
    as the last element of that list'''
    if len(list1)==len(list2):
        return False
    elif len(list1)>len(list2):
        list=list1
    elif len(list1)<len(list2):
        list=list2
    print(f"{list} is the longer list and its last element is {list.pop()}")


def main():
    if print_longer(['chocolate', 'vanilla'], [1, 5, 9, 7])==False:
        print("The lists are the same length!")


if __name__ == "__main__":
    main()

