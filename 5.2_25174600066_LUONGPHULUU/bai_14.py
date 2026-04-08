n = int(input("Nhập n: "))
A = []
for i in range(n):
    name = input("Ten: ")
    age = int(input("Tuoi: "))
    score = float(input("Diem: "))
    A.append((name, age, score))
for i in range(len(A)):
    for j in range(len(A) - i - 1):
        a = A[j]
        b = A[j + 1]
        if (a[0] > b[0]) or \
           (a[0] == b[0] and a[1] > b[1]) or \
           (a[0] == b[0] and a[1] == b[1] and a[2] > b[2]):
            A[j], A[j+1] = A[j+1], A[j]
print("Kết quả:")
for item in A:
    print(item)