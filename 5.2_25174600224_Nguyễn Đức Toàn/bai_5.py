A=[]
i=1
while i<=9999:
    if i%7!=0:
        A=A+[i] 
    i+=1

for x in A:
    print(x, end=" ")