def main():
    x = get_number()
    if is_even(x):
        print("EVEN")
    else:
        print("ODD")

def is_even(n):
    return  n % 2 == 0 

def get_number():
    while True:
        try:
            value = int(input("Enter the the value "))
            if value >0:
                return value
        except :
             print("Invalid number")
main()