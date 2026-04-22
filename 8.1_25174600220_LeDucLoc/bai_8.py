"""Bài 8: Viết chương trình tính chu vi và diện tích của: hình tròn, hình vuông, hình
chữ nhật và hình tam giác. Lưu ý: kiểm tra đầy đủ các trường hợp."""

def hinh_tron():
    r = float(input("Nhập bán kính hình tròn: "))
    if r > 0:
        cv = 2 * 3.14 * r
        dt = 3.14 * (r ** 2)
        print(f"=> Chu vi: {cv:.2f}, Diện tích: {dt:.2f}")
    else:
        print("Lỗi: Bán kính phải lớn hơn 0!")

def hinh_vuong():
    a = float(input("Nhập cạnh hình vuông: "))
    if a > 0:
        print(f"=> Chu vi: {4 * a}, Diện tích: {a * a}")
    else:
        print("Lỗi: Cạnh phải lớn hơn 0!")

def hinh_chu_nhat():
    dai = float(input("Nhập chiều dài: "))
    rong = float(input("Nhập chiều rộng: "))
    if dai > 0 and rong > 0:
        print(f"=> Chu vi: {(dai + rong) * 2}, Diện tích: {dai * rong}")
    else:
        print("Lỗi: Các cạnh phải lớn hơn 0!")

def hinh_tam_giac():
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))
    
    # Kiểm tra điều kiện tồn tại tam giác
    if a > 0 and b > 0 and c > 0:
        if (a + b > c) and (a + c > b) and (b + c > a):
            cv = a + b + c
            p = cv / 2 # Nửa chu vi
            # Tính diện tích theo công thức Heron
            dt = (p * (p - a) * (p - b) * (p - c)) ** 0.5
            print(f"=> Chu vi: {cv}, Diện tích: {dt:.2f}")
        else:
            print("Lỗi: Ba cạnh không tạo thành một tam giác!")
    else:
        print("Lỗi: Các cạnh phải lớn hơn 0!")

        
def main():
    print("----- CHỌN HÌNH CẦN TÍNH -----")
    print("1. Hình tròn")
    print("2. Hình vuông")
    print("3. Hình chữ nhật")
    print("4. Hình tam giác")
    
    lua_chon = input("Nhập lựa chọn của bạn (1-4): ")
    
    if lua_chon == '1':
        hinh_tron()
    elif lua_chon == '2':
        hinh_vuong()
    elif lua_chon == '3':
        hinh_chu_nhat()
    elif lua_chon == '4':
        hinh_tam_giac()
    else:
        print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()