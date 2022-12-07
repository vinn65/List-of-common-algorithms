#Explanation done here -- https://favtutor.com/blogs/counting-sort-python

def Countingsort(my_arr):
    n = len(my_arr)
    output = [0] * n
    count = [0] * 10
    # storing the count of each element 
    for m in range(0, n):
        count[my_arr[m]] += 1
    # storing the cumulative count
    for m in range(1, 10):
        count[m] += count[m - 1]
    # place the elements in output my_array after finding the index of each element of original my_array in count my_array
    m = n - 1
    while m >= 0:
        output[count[my_arr[m]] - 1] = my_arr[m]
        count[my_arr[m]] -= 1
        m -= 1

    for m in range(0, n):
        my_arr[m] = output[m]



l = int(input("Enter the number of elements in your array:"))
print("Enter the elements of your array and press enter after each element:")

my_arr = []
for i in range(0, l):
    item = int(input())
    my_arr.append(item)
    
n = len(my_arr)
print("Your unsorted list: ", my_arr)
Bubblesort(my_arr)
print("Your sorted list:",my_arr)
