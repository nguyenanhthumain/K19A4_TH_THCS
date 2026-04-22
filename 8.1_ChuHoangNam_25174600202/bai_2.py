#cau2
def in_fibonacci():
    a = 0
    b = 1
    
    print("Day 20 so Fibonacci la:")
    
    for i in range(20):
        print(a, end=" ")
        
        tam = a + b
        a = b
        b = tam
in_fibonacci()