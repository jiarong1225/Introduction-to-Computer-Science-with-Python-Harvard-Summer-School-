
# Make power(x, n) more efficent by computing
# power(x, n//2) (once!) instead of
# power(x, n-1) when n is even
def power(x, n):
    print(f"In power({x}, {n})")
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    smaller_case=power(x,n//2)
    if n % 2 == 0:
        return smaller_case *smaller_case
    else:
        return x * smaller_case * smaller_case


def main():
    print(power(2, 1024))  # should not crash
    print(power(3, 4))     # should print 81

if __name__ == "__main__":
    main()
