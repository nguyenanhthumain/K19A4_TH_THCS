#bai5
def ascii():
    s=""
    while True:
        c=input()
        if ord(c)==27:
            break
        s=s+str(ord(c))+" "
    return s

print(ascii())