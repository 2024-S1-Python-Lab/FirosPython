list1=[]
n=int(input("Enter the number of elements"))
for i in range(0,n):
    elem=int(input())

    list1.append(elem)

#List1=[2,4,-6,-8,9,7]
List2=[]
for i in list1:
    if i > 0:
        List2.append(i)
print(f"POSITIVE LIST={List2}")
