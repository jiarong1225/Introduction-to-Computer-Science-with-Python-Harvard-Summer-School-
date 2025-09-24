def selection_sort(data):
    for n in range(len(data)-1):
        my_list=data[n+1:]
        index_min=n+1+my_list.index(min(my_list))
        if data[n]>data[index_min]:
            swap(data,n,index_min)


def swap(data,i,j):
    data[i],data[j]=data[j],data[i]
    """
    Sorts the list data using selection sort. Returns Nothing.
    """
    # Add your code here


def main():
    nums = [ 3, 1, 4, 1, 5, 9]
    selection_sort(nums)
    print(nums)
    # Add your solution to the problem that makes use of
    # the above to sort a list.


if __name__ == "__main__":
    main()
