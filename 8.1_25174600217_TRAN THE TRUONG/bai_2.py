def in_fibonacci():
    so_luong = 20
    f0 = 0
    f1 = 1

    print("Dãy Fibonacci (tối đa 20 số):")

    print(f0, f1, end=" ")

    for i in range(2, so_luong):
        fn = f0 + f1
        print(fn, end=" ")
        f0 = f1
        f1 = fn
in_fibonacci()