class Object:
    ...

def main():
    problem = solve_problems()
    print(problem.area)


def solve_problems():
    problem = Object()
    area = int(input("lenght: ")) * int(input("Breadth: "))
    problem.area = area
    perimeter = int(input("lenght: ")) + int(input("Breadth: "))
    problem.perimeter = perimeter
    square = int(input("length "))**2
    problem.square = square
    
    return problem






if __name__ == "__main__":
    main()