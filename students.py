#to access the element in the read file
"""with open("students.csv") as file:
    for line in file: 
        first_name, last_name  = line.rstrip().split(",")
        print(f"{first_name}\t{last_name}") """
        
#to access the element sorted
"""students = []
with open("students.csv") as file:
    for line in file:
        first_name, last_name = line.rstrip().rsplit(",")
        students.append(f"{first_name} \t {last_name}")
        # print(first_name, last_name)
 
print(f"firstName \tLastName")       
for name in sorted(students):
    print(name)"""
    
    
# USING DICTIONARY TO SAVE THE DATA FROM CSV
"""students = []
with open("students.csv")as file:
    for line in file:
        first_name, last_name = line.rstrip().rsplit(",")
        student = {"First Name": first_name, "Last Name":last_name}
        students.append(student)"""
        
"""def get_name(student):
    return student["First Name"]
    # instead of using this function get_name, it is better 
    # we use lambda """
    
import csv

"""you can use the API from csv file to 
    manipulate the data in your file"""
# students = []
# with open("students.csv")as file:
#     reader = csv.reader(file)
#     for name, name2, state in reader:
#         students.append({"First Name": name,"State": state})
        
# for student in sorted(students, key = lambda student: student['First Name']):
#     print(f"First name is : {student['First Name']} and \tState is {student["State"]}")
    
"""Using a dictionary reader is the best way to acess and maniputlate   
    values in file"""
    
students = []
with open("students.csv")as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"First Name": row["First Name"],"State": row["State"]})
        
for student in sorted(students, key = lambda student: student['First Name']):
    print(f"First name is : {student['First Name']} and \tState is {student["State"]}")
    