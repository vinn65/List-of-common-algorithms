#Explanation done here -- https://stackabuse.com/bucket-sort-in-python/


def Bucketsort(my_arr):

    

l = int(input("Enter the number of elements in your array:"))
print("Enter the elements of your array and press enter after each element:")

my_arr = []
for i in range(0, l):
    item = int(input())
    my_arr.append(item)
    
n = len(my_arr)
print("Your unsorted list: ", my_arr)
print("Your sorted list:",Bucketsort(my_arr))