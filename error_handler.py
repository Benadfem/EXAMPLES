"""write a python program to test error handling """

# we inplement different ways to inprove on this program by 
# x = int(input("What's X? "))
# print(f"X is {x}")

#the above code will raise an error message ValueError which should be treated as this
# try:
#     x = int(input("What's X? "))    
# except ValueError:
#     print("X is not an integer")
# print(f"X is {x}")

"""and yet another error arises called NameError
such should be handled accrodingly """

# try:
#     x = int(input("What's X? "))    
# except ValueError:
#     print("X is not an integer")
# else:
#     print(f"X is {x}")

"""the code works perfectly
what if we want the user to correct herself without leaving the program """

# while True:
#     try:
#         x = int(input("What's X? "))    
#     except ValueError:
#         print("X is not an integer")
#     else:
#         break
# print(f"X is {x}")

"""instead of using plenty of code, we can reduce the line of code by the folowing """
# while True:
#     try:
#         x = int(input("What's X? ")) 
#         break   
#     except ValueError:
#         print("X is not an integer")

# print(f"X is {x}")

""""the program can reconstructed trying to absorb the error message
"""

# while True:
#     try:
#         print()
#         x = int(input("What's X? ")) 
        
#         break   
#     except ValueError:
#         pass #this line will absorb the error text expected to be shown to the user 


"""it is a good practice of code to create a main() fuction
    and put every single action in a function
    so as to create reusability of code or ordered adjustment to code """

def main():
    print(f"X is {get_value()}")

# this method uses return keyword because it only fetches value and gives it back to the user 
def get_value():
    while True:
        try:
            print()
            x = int(input("What's X? ")) 
            break   
        except ValueError:
            pass #this line will absorb the error text expected to be shown to the user 
    return x 

main()