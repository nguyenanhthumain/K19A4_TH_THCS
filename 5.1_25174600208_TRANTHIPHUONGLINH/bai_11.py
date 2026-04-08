n = int(input())
test = []
search = []
for i in range(n):
    x = int(input())
    y = int(input())
    test.append((x,y))
for i in range(n):
    x = int(input())
    y = int(input())
    search.append((x,y))
for i in search:
    if i in test:
        print(test.index(i))