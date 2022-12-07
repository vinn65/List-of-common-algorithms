#Explanation done here -- https://favtutor.com/blogs/counting-sort-python
def Countingsort(my_arr):
    soln = [0] * n

    count = [0] * 256
    
    for i in range(0, n):
        count[my_arr[i]] += 1
    for i in range(1, 256):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        soln[count[my_arr[i]] - 1] = my_arr[i]
        count[my_arr[i]] -= 1
        i -= 1

    for i in range(0, n):
        my_arr[i] = soln[i]



l = int(input("Enter the number of elements in your array:"))
print("Enter the elements of your array and press enter after each element:")

my_arr = []
for i in range(0, l):
    item = int(input())
    my_arr.append(item)
    
n = len(my_arr)
print("Your unsorted list: ", my_arr)
Countingsort(my_arr)
print("Your sorted list:",my_arr)
