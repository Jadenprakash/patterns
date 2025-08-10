r=int(input("enter your number of rows"))
space=r-1
for i in range (1,r+1):
    for j in range (1,space+1):
        print(end=" ")
    space=space-1    
    for j in range (2*i-1):
        print(end="#")
    print()