r = int(input("enter the total number of rows: "))
print("mirrored right angle triangle")
for i in range (1, r+1):
    for j in range (1, r +1 ):
        if j<= r- i :
            print('  ' ,end= '  ')
        else:
            print("*",end = "  ")
    print()