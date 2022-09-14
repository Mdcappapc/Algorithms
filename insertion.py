def insertion_sort(arr,):    
    for i in range(len(arr)):
        cursor = arr[i]
        pos =i
        while pos > 0 and arr[pos - 1] > cursor:
            arr[pos] = arr[pos - 1]
            pos -=1
        arr[pos] = cursor

    return arr
print(insertion_sort([6,5,3,1,4,7,2,9,8]))