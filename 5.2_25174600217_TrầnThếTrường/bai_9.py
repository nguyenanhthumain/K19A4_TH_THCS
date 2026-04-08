n = int(input("Nhập số lượng phần tử: "))
a = [int(input(f"a[{i}] = ")) for i in range(n)]
for x in a:
    assert x % 2 == 0, f"Phát hiện số lẻ: {x}"

print("Tất cả các số trong list đều là số chẵn.")