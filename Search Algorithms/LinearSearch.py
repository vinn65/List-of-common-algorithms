#Finding the maximum value using linear search
def linearsearch(n,my_arr,max_value):
    for i in range(0,n):
        if my_arr[i] > max_value:
            max_value = my_arr[i]
        index_value = my_arr.index(max_value)    
    print("The maximum value is {} at index {}".format(max_value,index_value))

# my_arr = [3,4,9,10,6,7,8]

l = int(input("Enter the number of elements in your array:"))
print("Enter the elements of your array and press enter after each element:")
my_arr = []
for i in range(0,l):
    item = int(input())
    my_arr.append(item)


max_value = my_arr[0]
n = len(my_arr)
linearsearch(n,my_arr,max_value)

    