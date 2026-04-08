"""Viết chương trình sinh dãy (list) A là biểu diễn của ma trận đơn vị. Chương trình
nhập số n từ bàn phím và sinh ra ma trận đơn vị bậc n, sau đó hiện kết quả trên
màn hình."""
n = int(input("Nhập bậc của ma trận đơn vị n: "))

ma_tran_don_vi = []

for i in range(n):
    hang = []
    for j in range(n):
        if i == j:
            hang.append(1)
        else:
            hang.append(0)
    ma_tran_don_vi.append(hang)

print(f"Ma trận đơn vị bậc {n}:")
for hang in ma_tran_don_vi:
    print(hang)