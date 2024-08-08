# Write a Python program to find the smallest missing number in a sorted list using a for-else loop.

def find_smallest_missing(arr):
    for i in range(len(arr)):
        if arr[i] != i:
            return i
    else:
        return len(arr)


arr = [0, 1, 2, 6, 9, 11, 15]
missing_number = find_smallest_missing(arr)
print("The smallest missing number is:", missing_number)
