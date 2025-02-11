n=int(input("enter a numer"))
temp = n
rem=0
num=0
print(n)
while n > 0:
    rem = n % 10
    num = num * 10 + rem
    n = n // 10
print(f"{num}")
if temp == num :
    print(f" {temp} is a palindrome")
else:
    print(f" {temp} is not a palindrome")
