def main():
    number = get_number()
    meon(number)

def get_number():
    while True:
        n = int(input("Enter the number "))
        if n > 0 :
            break
        else: 
            print("Enter a valid number ")
    return n

def meon(x):
    for _ in range(x):
        print("MEON")

main()