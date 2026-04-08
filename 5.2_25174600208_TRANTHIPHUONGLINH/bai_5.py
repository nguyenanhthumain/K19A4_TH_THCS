A=[]
x=1
while len(A)<1000:
    if x%7!=0:
        A.append(x)
    x+=1
print("1000 số ko chia hết 7:", A)