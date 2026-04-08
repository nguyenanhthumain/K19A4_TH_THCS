s = input("Nhập chuỗi: ")
start = 0
while start < len(s) and s[start] == ' ':
    start += 1
end = len(s) - 1
while end >= 0 and s[end] == ' ':
    end -= 1
s = s[start:end+1]
result = []
i = 0
while i < len(s):
    if s[i] != ' ':
        result.append(s[i])
    else:
        if len(result) > 0 and result[-1] != ' ':
            result.append(' ')
    i += 1
normalized = ''.join(result)
print("Chuỗi sau khi chuẩn hóa:")
print(normalized)