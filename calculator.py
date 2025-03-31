
"""A program that gets the square of a number """
def main():
    x = float(input("What is the value of X? "))
    print(f"the square of X is {square(x)}")

def square(n):
    return n * n

if __name__ == "__main__":
    main()