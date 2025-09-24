"""Add your solution to the problem 'letters' here."""


def missing_letters(word_list):
    words_list=list(word_list)
    letter_list=[]
    for x in words_list:
        letter_list+=list(x)
    for y in range(len(letter_list)):
        letter_list[y]=letter_list[y].upper()
    letter_number=[ord(i) for i in letter_list]
    missing_letter=[]
    for y in range(65,91):
        if y not in letter_number:
            missing_letter+=chr(y)
    print(missing_letter)

    """Takes a word list and returns a sorted
    list of letters, capitalized that do not appear
    in the list.
    """
    # Add your code here.


def main():
    # Add your solution to the problem that makes use of the above.
    missing_letters(["Now", "is", "the", "TIME"])



if __name__ == "__main__":
    main()
