#wap to create a list from an existing list by removing all odd no

list1 = []
n = int(input("Enter n: "))
for i in range(n):
    list1.append(int(input("Enter no.")))
#list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [item for item in list1 if item%2 == 0]
print(list2)
