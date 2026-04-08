"""15. Viết một chương trình có 2 chữ số, X, Y nhận giá trị từ đầu vào và tạo ra một
mảng 2 chiều. Giá trị phần tử trong hàng thứ i và cột thứ j của mảng phải là i*j. Lưu
ý: i=0,1,.., X-1; j-0,1,.., Y-1. Ví dụ: Giá trị X, Y nhập vào là 3, 5 thì đầu ra là: 110, 0,
0, 0, 01, [0, 1, 2, 3, 41, [0, 2, 4, 6, 8]]."""

X = int(input("Nhập số X: "))
Y = int(input("Nhập số Y: "))
a = [[i * j for j in range(Y)] for i in range(X)]
print(a)