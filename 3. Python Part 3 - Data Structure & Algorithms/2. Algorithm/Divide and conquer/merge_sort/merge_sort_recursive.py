#import time

def merge_sort(arr):
    if len(arr)>1:
        left_arr = arr[:(len(arr) // 2)]
        right_arr = arr[len(arr) // 2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = 0  # left_arr idx
        j = 0  # right_arr idx
        k = 0  # merged arr idx

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i<len(left_arr):
            arr[k] = left_arr[i]
            k+=1
            i+=1

        while j<len(right_arr):
            arr[k] = right_arr[j]
            k+=1
            j+=1


#start = time.time_ns()
array = [1,45,6,75,33,8,5,7,3,12,8,9]
merge_sort(array)
#end = time.time_ns()
#print(f"{(end-start)}")
print(array)