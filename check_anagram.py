#program for anagram

i = (input())
j = (input())
if(len(i) != len(j)):
    print("Length not match")
else:
    lst1 = [item for item in i]
    lst2 = [item for item in j]
    
    for i in lst2:
        if(i in lst1):
            lst1.remove((i))

    if(len(lst1) == 0):
        print("Anagram Number")
    else:
        print("Not Anagram")
        