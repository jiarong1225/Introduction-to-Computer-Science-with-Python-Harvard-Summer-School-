

def average_digit(data, label):
    digit_list=[ [0] * 28 for i in range(27)]
    for j in range(27):
        sum=0
        count=0
        for i in range(27):
            for n in range(len(data)-1):
                if data[n][label]==3:
                    data_list=data[n]['data']
                #this line defines that data_list(n) is the place we are in
                    data_line=data_list[i]
                    #data_line(i) is the line in data_list(n) we are in
                    sum+=data_line[j]
                    #we add the value in position j in data_line(i) to the sum of (i,j)
                    count+=1
            average=sum/count
            digit_list[i][j]=int(average)
    return digit_list


    """Compute and return the average 28x28 grayscale digit with the
    given label in the mnist dataset.
    """
    # Add your code here


def main():
    # Add your solution to the problem that makes use of
    # the above to sort a list.
    from mnist_data import items
    average_3 = average_digit(items,'label')
    for each_list in average_3:
        print(each_list)


if __name__ == "__main__":
    main()




