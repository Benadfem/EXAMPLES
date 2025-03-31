class Student:
    def __init__(self, name, house, Patronious):
        if not name:
            raise ValueError ("Missing Name")
        if  house not in ["Babaode", "Onibuku", "Atan","Winners"]: 
            raise ValueError ("Not found House! ")                
        self.name = name
        self.house = house
        self.Patronious = Patronious
        
    def __str__(self):
        return f"Name: 👩 {self.name} House: 🏛  {self.house} "
    
    def charm(self):
        match self.Patronious:
            case "Stag":
                return "👺"
            case "shabba":
                return "🤑"
            case "otter" :
                return 

def main():
    
    student = get_student()
    # print(f"Name:  {student.name} House:   {student.house}")
    print(student)
    
    
    
def get_student():    
    name = input("Name: ").title()
    house = input("House: ").title()
    Patronious = input("Patronious: ").title()
    return Student(name, house,Patronious)
    









if __name__ == "__main__":
    main()