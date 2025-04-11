def quicksort(arr, left, right):
    if left<right:
        print(arr[left:right])
        pi = partition(arr,left,right)
        quicksort(arr,left,pi-1)
        quicksort(arr,pi+1,right)




def partition(arr,left,right):
    pivot = arr[right]

    i = left-1

    for j in range(left, right):
        if arr[j] <= pivot:
            i+=1
            arr[j],arr[i] = arr[i], arr[j]

    arr[i+1], arr[right] = arr[right], arr[i+1]

    return i+1


def quicksort_listcomprehesion(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [i for i in arr[1:] if i<=pivot]
        greater_than_pivot = [i for i in arr[1:] if i>pivot]
        return quicksort(less_than_pivot)+[pivot]+quicksort(greater_than_pivot)






arr = [0,3,6,62,5,2,6,7,23,526,7]
quicksort(arr,0,len(arr)-1)

print(arr)

