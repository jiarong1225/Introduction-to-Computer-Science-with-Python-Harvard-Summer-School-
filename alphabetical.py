def alphabetical(words):
    for i in range(len(words)):
        word_list=list(words[i])
        word_list.sort()
        words[i]="".join(word_list)
    return(words)


def main():
    print(alphabetical(['apple', 'pumpkin', 'log', 'River', 'fox', 'pond']))


if __name__ == "__main__":
    main()
