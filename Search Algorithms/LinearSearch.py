# In this program, Linear search is implimented in two ways:Finding the maximum value in an array, Finding a specific element
#finding the maximum value
def linearsearch(n,my_arr,max_value):
    for i in range(0,n):
        if my_arr[i] > max_value:
            max_value = my_arr[i]
        index_value = my_arr.index(max_value)    
    print("The maximum value is {} at index {}".format(max_value,index_value))
#finding a specific element.
def linearsearch1(n,my_arr):
    value = int(input("Enter a number to search for:"))
    for i in range(0,n):
        if my_arr[i] == value:
            value = my_arr[i]
        index_value = my_arr.index(value)    
        print("{} was found at index {}".format(value,index_value))
        break
    else:
        print("{} not found!".format(value))

l = int(input("Enter the number of elements in your array:"))
print("Enter the elements of your array and press enter after each element:")


my_arr = []
for i in range(0,l):
    item = int(input())
    my_arr.append(item)


max_value = my_arr[0]

n = len(my_arr)

print("1.Find a specific element 2.Find the maximum value")
choice = int(input("Enter an operation to perform: 1 or 2:"))

if choice == 1:
    linearsearch1(n,my_arr)
elif choice == 2:
    linearsearch(n,my_arr,max_value)
else:
    print("Please enter either 1 or 2")


    
