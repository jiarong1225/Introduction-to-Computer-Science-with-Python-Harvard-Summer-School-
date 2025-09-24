def is_vowel(c):
    vowels='aeiouAEIOU'
    if c in vowels:
        return True
    else:
        return False


def devowel(ad):
    ad_word=ad.split(" ")
    devowel_sentence=[]
    for n in range(len(ad_word)):
        devowel_sentence.append(devowel_one_word(ad_word[n]))
    return " ".join(devowel_sentence)


def devowel_one_word(word):
    word_list=list(word)
    devowel_one=word_list[0]
    for i in range(1,len(word_list)):
        if is_vowel(word_list[i])==False:
            devowel_one+=word_list[i]
    return("".join(devowel_one))


def main():
    print(devowel(input("a normal one-line description of a property: ")))

if __name__ == "__main__":
    main()
