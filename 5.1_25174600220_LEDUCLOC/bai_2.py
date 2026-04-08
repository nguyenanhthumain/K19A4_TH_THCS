#Bài 2 Viết một chương trình tạo danh sách (List) chứa các giá trị bình phương của các số từ 1 đến n (bao gồm cả 1 và n với n được nhập từ bàn phím) và in ra toàn bộ danh sách đó trừ m kết quả đầu tiên trong danh sách (m được nhập từ bàn phím). Nếu m ≥ n thì trả về một danh sách rỗng.
n = int(input("Nhập n: "))
m = int(input("Nhập m: "))
list = []
for i in range(1,n+1):
    
    list.append(i**2)

if m < n:
    print(list[m:])

else:    
    print([])