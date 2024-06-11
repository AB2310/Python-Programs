i=0
for i in range(0,10):
    for j in range(10-i):
        print(" ",end="")
    for k in range(1,i):
        print(" *",end="") 
    print()