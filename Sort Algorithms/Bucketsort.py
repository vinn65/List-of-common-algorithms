#Explanation done here -- https://stackabuse.com/bucket-sort-in-python/

#Insertion is another type of sort algorithms. Here it`s used to sort elements in bucket
def Insertionsort(bucket):
    for i in range (1, len(bucket)):
        var = bucket[i]
        j = i - 1
        while (j >= 0 and var < bucket[j]):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var
   

l = int(input("Enter the number of elements in your array:"))
print("Enter the elements of your array and press enter after each element:")

my_arr = []
for i in range(0, l):
    item = int(input())
    my_arr.append(item)
    
n = len(my_arr)
print("Your unsorted list: ", my_arr)
print("Your sorted list:",Bucketsort(my_arr))