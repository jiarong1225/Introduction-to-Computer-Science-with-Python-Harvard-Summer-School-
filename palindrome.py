

def is_palindrome(a_string):
    string=a_string.lower()
    string_list=list(string)
    if len(string_list)<=1:
        return True
    elif string_list[0]==string_list[-1]:
        string_list.pop(-1)
        string_list.pop(0)
        return is_palindrome(''.join(string_list))
    else:
        return False
    ''' Should return True exactly when a_string is a
    palindrome, ignoring case.
    '''

def main():
    print(is_palindrome("Foobar")) # should be False
    print(is_palindrome("Kayak"))  # should be True

if __name__ == "__main__":
    main()
