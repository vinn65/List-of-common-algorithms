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
def Bucketsort(my_arr):
    
    maxValue = max(my_arr)
    size = maxValue/n

    buckets = []
    for x in range(n):
        buckets .append([]) 
    for i in range(n):
        j = int (my_arr[i] / size)
        if j != n:
            buckets [j].append(my_arr[i])
        else:
            buckets [n - 1].append(my_arr[i])
    for z in range(n):
        Insertionsort(buckets[z])

    final_output = []
    for x in range(len (my_arr)):
        final_output = final_output + buckets [x]
    return final_output
   

l = int(input("Enter the number of elements in your array:"))
print("Enter the elements of your array and press enter after each element:")

my_arr = []
for i in range(0, l):
    item = int(input())
    my_arr.append(item)
    
n = len(my_arr)
print("Your unsorted list: ", my_arr)
print("Your sorted list:",Bucketsort(my_arr))