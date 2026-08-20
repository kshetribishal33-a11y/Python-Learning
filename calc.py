#Day 3 as a learning python
#Mini-Project: Calculator that can preform:
# +,-,/,*,**,//,%

a=int(input("Enter the 1st num: "))
b=int(input("Enter the 2nd num: "))
op=input("Enter the operator(+,-,/,*,**,//,%) ")

if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
elif op=="/":
    print(a/b)
elif op=="**":
    print(a**b)
elif op=="//":
    print(a//b)
elif op=="**":
    print(a**b)
else:
    print("ENVALID OPERATION!")