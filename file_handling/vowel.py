

vowel_cnt = 0
with open('./file_handling/demo.txt','r') as f:
    data = f.read()
    for item in data:
        if item.lower() == 'a' or item.lower() == 'e' or item.lower() == 'i' or item.lower() == 'o' or item.lower() == 'u':
            vowel_cnt += 1

print("Total vowel = ",vowel_cnt)

