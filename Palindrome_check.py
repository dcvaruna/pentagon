n = int(input("enter a numer"))
temp = n
rem = 0
num = 0
while n > 0:
    rem = n % 10
    num = num * 10 + rem
    n = n // 10
    
if temp == num :
    print(f" {temp} is a palindrome")
else:
    print(f" {temp} is not a palindrome")

print( "inside the new branch")