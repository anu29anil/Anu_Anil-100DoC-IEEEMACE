list1=[1,2,3]
numbers=input("Enter the number:")
for i in numbers:
    if i.isdigit():
        inp=int(i)
        list1.append(inp)
    else:
        continue
    
print(list1)
