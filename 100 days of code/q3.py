list1=[1,2,3]
numbers=eval(input("Enter the number:"))
if type(numbers)==int:
    list1.append(numbers)
else:
    for i in numbers:
        inp=int(i)
        list1.append(inp)
    
print(list1)
