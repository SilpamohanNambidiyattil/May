a = ["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
print("Given list:", a)
x = str(a[0])
c = str(a[1])
v = str(a[2])
b = str(a[3])

y1 = x[x.index('.') + 9: ]
y2 = c[c.index('.') + 11:]
y3 = v[v.index('.') + 5:]
y4 = b[b.index('.') + 6:]

print("using indexing:", y1, y2, y3, y4)

a1 = x.split('.')[-1]
a2 = c.split('.')[-1]
a3 = v.split('.')[-1]
a4 = b.split('.')[-1]
print("using split:", a1, a2, a3, a4)
