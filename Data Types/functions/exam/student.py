n=[78,88,80,34,56,97,91]
def less(n):
    if n<80:
        return True
    return False
l80 = filter(less,n)
print(list(l80))