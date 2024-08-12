# wap to input a string and a number n and print only those characters whose length is greater that number

str1 = input("Enter String: ")
list1 = str1.split()
n = int(input("Enter n: "))
list2 = []
for i in list1:
    if len(i) >= n:
        list2.append(i)
print(list2)
        
