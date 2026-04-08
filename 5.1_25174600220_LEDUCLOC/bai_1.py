#1. Viết một chương trình tạo danh sách (List) chứa các giá trị bình phương của các số từ 1 đến n (bao gồm cả 1 và n với n được nhập từ bàn phím) và in m mục đầu tiên trong danh sách (m được nhập từ bàn phím).Nếu m ≥ n thì in ra toàn bộ danh sách kết quả
n = int(input("Nhập n: "))
m = int(input("Nhập m: "))
list = []   
for i in range(1,n+1):
    list.append(i**2)
if m <= n:
    print(list[:m])
else:    
    print(list)