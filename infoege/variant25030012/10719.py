from time import sleep

s = open('files/17_10719.txt').read()
s = s.split()

cnt = 0
i = 0
res = []
for member in s:
    if (s[i][len(s[i]) - 2: len(s[i])] == '13' and s[i + 3][len(s[i + 3]) - 2: len(s[i + 3])] != '13')  or (s[i][len(s[i]) - 2: len(s[i])] != '13' and s[i + 3][len(s[i + 3]) - 2: len(s[i + 3])] == '13'):
        cnt += 1
        res += [int(s[i]) + int(s[i + 3])]
    if i + 1 < len(s) - 3:
        i += 1

print(cnt)
print(max(res))
