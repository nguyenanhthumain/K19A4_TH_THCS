print("Bắt đầu nhập số (Chương trình dừng nếu nhập số âm hoặc số thập phân):")
while True:
    user_input = input("Nhập một số: ")
    num = float(user_input)
    if num < 0 or num != int(num):
        print("Đã gặp số âm hoặc số thập phân. Dừng chương trình.")
        break
    print(f"Bạn vừa nhập số nguyên: {int(num)}")