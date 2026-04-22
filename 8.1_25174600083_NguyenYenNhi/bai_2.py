#bai_2
"""
Biết rắng dãy số Fibonacci là dãy số vô hạn, được bắt đầu bởi số 0 và số 1, 
các số tiếp theo luôn bằng tổng của 1 số liền trước cộng lại. Ví dụ: 0, 1, 1, 2,
3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610... Yêu cầu: Viết hàm tìm và in ra
màn hình dãy Fibonacci không quá 20 số hạng (Hàm không có giá trị trả về).
"""

def fibonacci(n):
    a, b = 0, 1
    so_hang = 0
    while so_hang < n:
        print(a, end=' ')
        a = b 
        b = a + b
        so_hang += 1
fibonacci(20)