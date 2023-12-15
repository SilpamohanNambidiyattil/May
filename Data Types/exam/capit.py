lines = []
while True:
    str1 = input()
    if str1=='':
        break
    else:
        lines.append(str1+'\n')
x = ''.join(lines)
for i in x:
    cap = x.upper()
print(cap)