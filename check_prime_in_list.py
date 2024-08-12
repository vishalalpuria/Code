# Wap to check if a list is having all prime numbers if a single element is not prime then print sum of all the element in the list

list1 = [1,2,3,5,7]
list2 = []
sum1 = 0
cnt = 0
for n in list1:
    i = 2
    f = True
    while(i<= n//2):
        if(n%i==0):
            f = False
            break
        i+=1
    if(f == True):
        list2.append(n)
        cnt += 1

if(cnt != len(list1)):
    for i in list1:
        sum1 += i
    print("Sum is", sum1)
else:
    print("All primes are", list2)


