"""Add your solution to the problem 'print_medals' here."""


def print_medals(medal_counts):
    print(f"{"Gold":>21}",end="\t")
    print(f"{"Silver":>5}",end="\t")
    print(f"{"Bronze":>5}",end="\t")
    print(f"{"Total":>5}",end="\n")
    for i, j in medal_counts.items():
        print(f"{i:>13}",end="\t")
        times=1
        for z in j:
            print(f"{z:>5}", end="\t")
            times+=1
        print(f"{sum(j):>5}")
    """Takes the a dictionary of medal counts and prints
    a nicely formatted table with totals for each country
    as described in the pset 5 problem.
    """
    # Add your code here.


def main():
    # Add your solution to the problem that makes use of the above.
    MEDAL_COUNTS = {
        "Canada": [0, 3, 0],
        "Italy": [0, 0, 1],
        "Germany": [0, 0, 1],
        "Japan": [1, 0, 0],
        "Kazakhstan": [0, 0, 1],
        "Russia": [3, 1, 1],
        "South Korea": [0, 1, 0],
        "United States": [1, 0, 1],
    }
    print_medals(MEDAL_COUNTS)


if __name__ == "__main__":
    main()
