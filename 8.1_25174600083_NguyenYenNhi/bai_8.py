#bai_8
"""
8: Viết chương trình tính chu vi và diện tích của: hình tròn, hình vuông, hình
chữ nhật và hình tam giác. Lưu ý: kiểm tra đầy đủ các trường hợp.
"""

def tinh_chu_vi_va_dien_tich() :
    r = float(input("Nhập bán kính hình tròn: "))
    if r < 0:
        print("Nhập lại")
        return
    else :
        chu_vi = 2 * 3.14 * r
        dien_tich = 3.14 * r**2
    print("Chu vi và diện tích hình tròn là: ", chu_vi,"và", dien_tich)

    a = float(input("Nhập cạnh hình vuông: "))
    if a < 0:
        print("Nhập lại")
        return
    else :
        chu_vi = 4 * a
        dien_tich = a**2
    print("Chu vi và diện tích hình vuông là: ", chu_vi,"và", dien_tich)


    b = float(input("Nhập chiều dài hình chữ nhật: "))
    c = float(input("Nhập chiều rộng hình chữ nhật: "))
    if b < 0 or c < 0:
        print("Nhập lại")
        return
    else :
        chu_vi = 2 * (b + c)
        dien_tich = b * c
    print("Chu vi và diện tích hình chữ nhật là: ", chu_vi,"và", dien_tich)

    canh_1 = float(input("Nhập độ dài cạnh thứ 1 của tam giác: "))
    canh_2 = float(input("Nhập độ dài cạnh thứ 2 của tam giác: "))
    canh_3 = float(input("Nhập độ dài cạnh thứ 3 của tam giác: "))
    if canh_1 < 0 or canh_2 < 0 or canh_3 < 0:
        print("Nhập lại")
        return
    else:
        chu_vi = (canh_1 + canh_2 + canh_3) / 2
        dien_tich = (chu_vi * (chu_vi - canh_1) * (chu_vi - canh_2) * (chu_vi - canh_3)) ** 0.5
    print("Chu vi và diện tích hình tam giác là: ", chu_vi,"và", dien_tich)
tinh_chu_vi_va_dien_tich()