from sys import argv
from random import randint

def main():
    list_both=argv[1:]
    outfile=list_both[0]
    try:
        num_ints=int(list_both[1])
        f = open(outfile, "x")
        for n in range(num_ints):
            i=str(randint(0,36))
            f.write(f'{i}\n')
        print(f"Successfully wrote {num_ints} random numbers to {outfile}")
        f.close()
    except:
        pass


if __name__ == "__main__":
    main()
