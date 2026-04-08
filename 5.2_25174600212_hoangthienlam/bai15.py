input_str = input("Nhập X, Y (cách nhau bởi dấu phẩy): ")
dimensions = [int(x) for x in input_str.split(',')]
hang = dimensions[0]
cot = dimensions[1]
mang_2_chieu = [[i * j for j in range(cot)] for i in range(hang)]
print(mang_2_chieu)