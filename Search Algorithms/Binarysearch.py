def Binarysearch(my_arr, x, low, high):
    while low <= high:
        mid = low + (high - low)//2
        if my_arr[mid] == x:
            return mid
        elif my_arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


l = int(input("Enter the number of elements in your array:"))
print("Enter the elements of your array and press enter after each element:")


my_arr = []
for i in range(0, l):
    item = int(input())
    my_arr.append(item)
    
n = len(my_arr)
x = int(input("Enter the element to search for:"))
result = Binarysearch(my_arr, x, 0, len(my_arr)-1)

if result != -1:
    print("{} found at index ".format(x) + str(result))
else:
    print("{} not in the array!".format(x))