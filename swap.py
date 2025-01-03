def swap(a,b):
    a,b=b,a
    print("Value inside the function a=",a,"b=",b)
    return a,b




a=int(input("Enter a "))
b=int(input("Enter b "))

print("function outside value  of a=",a,"b=",b)
a,b=swap(a,b)

