n = int(input())
test_list = []
for i in range(n):
    a = int(input())
    b = int(input())
    test_list.append((a, b))
search_tup = []
for i in range(n):
    a = int(input())
    b = int(input())
    search_tup.append((a, b))
for tup in search_tup:
    found = False
    for i in range(len(test_list)):
        if test_list[i] == tup:
            print(i)
            found = True
            break
    if not found:
        print(-1)