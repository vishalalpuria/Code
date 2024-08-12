# Given a list of numbers, use a while loop to find the maximum number in the list.

list1 = [5, 10, 3, 8, 2]
m_no = list1[0]
index = 1

while index < len(list1):
    if list1[index] > m_no:
        m_no = list1[index]
    index += 1

print("The maximum number is:", m_no)

