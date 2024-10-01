with open("file_handling/demo.txt", 'r') as f:
    data = f.read()
    data = data.split()

flag = 0

for item in data:
    if "hack" in item.lower():
        flag = 1
        break
if flag:
    print("Hack present ")
else: 
    print("Hack not present")