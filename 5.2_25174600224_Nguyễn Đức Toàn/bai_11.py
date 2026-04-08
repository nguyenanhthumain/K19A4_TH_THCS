n=int(input("Nhập n: "))
A=[int(input(f"Nhập phần tử {i+1}: ")) for i in range(n)]

B=[x for x in A if x%3==0 and x%5!=0]
print("Danh sách B:", B)

C=[x**2 for x in A]
print("Danh sách C:", C)

D=[x for x in A if x%3==0]
print("Danh sách D:", D)