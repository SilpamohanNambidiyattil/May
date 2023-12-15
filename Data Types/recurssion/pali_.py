""" Palindrome  """
n = int(input("enter a number:"))
def pali(n):
    def reverse(n, rev=0):
        if n == 0:
            return rev
        else:
            a=((rev * 10) + (n % 10))
            rev = reverse(n // 10, a)
            return rev
    if reverse(n)==n:
        print("palindrome")
    else:
        print("not palindrome")
print(pali(n))

""" String """
string=input("Enter a string:")
print(string[1:-1])
def pa(string):
    def rev(string):
        if len(string) == 0:
            return string
        else:
            re = rev(string[1:]) + string[0]
            return re
    if rev(string)==string:
        print("Palindrome")
    else:
        print("not palindrome")
print(pa(string))

""" Another method"""
def pal(string):
    if len(string)<=1:
        return True
    else:
        if string[0]==string[-1]:
            pa = pal(string[1:-1])
        else:
            return False
print(pal(string))