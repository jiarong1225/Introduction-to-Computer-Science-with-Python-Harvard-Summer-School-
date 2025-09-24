
# change this to recursively print
# an upside-down triangle
def print_triangle(side_length):
    if side_length < 1:
        return
    print_triangle(side_length-1)
    print("[]" * (5-side_length))

def main():
    print_triangle(4)

if __name__ == "__main__":
    main()
