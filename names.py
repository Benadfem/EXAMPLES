
for i in range (1, 5):
    name = input("What's your name? ")
    with open( "names.txt","a") as file:        
        file.write(f"{name}\n")

#for me to read the data or file that has been created, and sort it 
names = []
with open("names.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    names.append(line.rstrip())

# for name in sorted(names):
#     print(f"Hello, {name}")
    
names.sort()
for name in names:
    with open("edited.txt", "a") as file:
        file.write(f"{name}\n")