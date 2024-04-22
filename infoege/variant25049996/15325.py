line = '8' * 45

while '1111' in line or '8888' in line:
    if '1111' in line:
        line = line.replace('1111', '88')
    else:
        line = line.replace('8888', '11')

print(line)
