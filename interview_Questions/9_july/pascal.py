def pattern(n):
    row = [1]
    for i in range(n):
        print(' '.join(str(x) for x in row))
        next_row = [1]
        for j in range(1,len(row)):
            next_row.append(row[j-1] + row[j])
        next_row.append(1)
        row=next_row


n = int(input("Enter the limit:"))
print(pattern(n))
