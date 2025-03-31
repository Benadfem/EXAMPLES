from calculator import square


def main():
    test_square()


def test_square():
    if square(2) != 4:
        print("there is an error")
    if square(3) != 9:
        print("there is an error")
    else:
        print("Program Successful!")

if __name__ == "__main__":
    main()

 