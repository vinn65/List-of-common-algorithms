def Bubblesort(my_arr):    
    for i in range(n-1):  
        for j in range(n-1):  
            if(my_arr[j] > my_arr[j+1]):  
                temp = my_arr[j]  
                my_arr[j] = my_arr[j+1]  
                my_arr[j+1] = temp  
    return my_arr 


l = int(input("Enter the number of elements in your array:"))
print("Enter the elements of your array and press enter after each element:")

my_arr = []
for i in range(0, l):
    item = int(input())
    my_arr.append(item)
    
n = len(my_arr)
print("Your unsorted list: ", my_arr)
print("Your sorted list:",Bubblesort(my_arr))