def sentence_type(sentence):
    '''Returns a string depending on the last character.'''
    last_word=list(sentence).pop()
    if last_word==".":
        return 'declarative'
    elif last_word=="?":
        return 'interrogative'
    elif last_word=="!":
        return 'exclamatory'
    else:
        return 'bad ending'


def main():
    print(sentence_type('Hi every body?'))


if __name__ == "__main__":
    main()

