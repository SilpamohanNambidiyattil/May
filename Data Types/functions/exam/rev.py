str1 = 'you are awesome'
st = [str[i] for i in range(len(str1)-1,-1,-1)]
print(''.join(st))