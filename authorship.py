"""Add your solution to the problem 'authorship' here."""

# make sure to import your data file here
import romeo_and_juliet_data
def word_length_histogram(text_list):
    word_length_counts = {i: 0 for i in range(1, 15)}
    for line in text_list:
        words = line.split()
        for word in words:
            length = len(word)
            if 1 <= length <= 14:
                word_length_counts[length] += 1
    return word_length_counts

    """Takes the a list of multiword lines and returns
    a dictionary where the keys are word lengths and the
    values are how many words there are of that length.
    Assume there is no punctuation to worry about.
    For example, the input:
        [ "Summer school", "is nearly over"]
    should return the dictionary
        { 6 : 3, 2 : 1, 4 : 1 }
    """
    # Add your code here.


def main():
    result = word_length_histogram(romeo_and_juliet_data.lines)
    total = sum(result.values())
    for j in result:
        proportion="{:.2f}".format(100*result[j]/total)
        print(f"Proportion of {j}-letter words: {proportion}% ({result[j]} words)")
    # Add your solution to the problem that makes use of the above to
    # print out the word length frequency table described in the pset.


if __name__ == "__main__":
    main()
