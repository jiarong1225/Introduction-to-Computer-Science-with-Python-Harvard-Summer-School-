def shift_one_char(c, offset):
    '''Applies a shift of offset to alphabetic
    ascii characters, as described in the problem set.
    Returns other characters unmodified'''
    if not c.isalpha() or c > 'z':
        return c
    if 'A' <= c <= 'Z':
        base = ord('A')
    elif 'a' <= c <= 'z':
        base = ord('a')

    return chr((ord(c) - base + offset) % 26 + base)

def shift_text(text, offset):
    '''Returns a string of all of the input text shifted by offset'''
    return "".join(shift_one_char(c, offset) for c in text)

def main():
    # You can add some test cases or other functionality here if you want
    text = "Hello, World!"
    shifted_text = shift_text(text, 3)
    print(shifted_text)

if __name__ == "__main__":
    main()
