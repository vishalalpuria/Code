# write a code to check freq of a particular word Ex. LPU
# abc.txt in d drive in mca folder

# case sensitive will be there 

import os
import re
cnt = 0
try:
    os.mkdir(r"D://MCA")
except:
    pass

with open("D://MCA//abc.txt","w") as f:
    s = "This is a test string\nThis is line LPU. 2 \"LPU\" in the abc.txt\nthis is line 3. (LPU- hello)"
    f.write(s)

with open("D://MCA//abc.txt","r") as f:
    data = f.read() 
    m = re.findall(r'LPU', data)
    cnt = len(m)

print(f"LPU = {cnt}")


