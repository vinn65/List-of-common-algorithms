def Insertionsort(my_arr):
    for i in range(1,n):
        key = my_arr[i]
        j = i - 1

        while j >= 0 and key < my_arr[j]:
            my_arr[j + 1] = my_arr[j]
            j = j - 1
        my_arr[j + 1] = key


l = int(input("Enter the number of elements in your array:"))
print("Enter the elements of your array and press enter after each element:")

my_arr = []
for i in range(0, l):
    item = int(input())
    my_arr.append(item)
    
n = len(my_arr)
print("Your unsorted list: ", my_arr)
Insertionsort(my_arr)
print("Your sorted list:",my_arr)
