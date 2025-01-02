print("pyramid of stars *")
rows = int(input("enter the number of rows that the base should have: "))
for i in range (rows):
    for j in  range (i+1):
     print("*", end=" ")
    print()