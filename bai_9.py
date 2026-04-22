def tinh(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b

def luy_thua(x, n):
    kq = 1
    for i in range(n):
        kq *= x
    return kq