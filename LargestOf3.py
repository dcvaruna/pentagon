a=int(input("enter the first number"))
b=int(input("enter the second number"))
c= int(input("enter the third number"))

if a>b and a>c:
    print(f"the largest of {a},{b} and {c} is {a}")
elif b>a and b>c:
    print(f"the largest of {a},{b} and {c} is {b}")
else:
    print(f"the largest of {a},{b} and {c} is {c}")