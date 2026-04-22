#bai_5
"""
Viết hàm nhập ký tự bất kỳ từ bàn phím, in ra màn hình giá trị ASCII của
ký tự đó, vòng lặp chỉ kết thúc khi nhấn phím ESC.
"""
def gia_tri_ASCII(ky_tu):
    return ord(ky_tu)
while True:
    ky_tu = input("Nhập một ký tự : ")
    if ky_tu == chr(27):
        break
    print(f"Giá trị ASCII là: {gia_tri_ASCII(ky_tu)}")