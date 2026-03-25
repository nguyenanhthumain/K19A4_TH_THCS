n = int(input("Nhap n: "))
s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0
s6 = 0

for i in range(1, n + 1):
    s1 = s1 + i**2                      
    s2 = s2 + (2*i + 1)**3               
    s3 = s3 + (2*i)**4                  
    s4 = s4 + ((-1)**(i-1)) / i          
    s5 = s5 + 1 / (i * (i + 1))         
    s6 = s6 + 1 / (i**0.5)    
               
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)