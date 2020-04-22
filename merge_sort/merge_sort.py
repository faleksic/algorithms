from math import floor


def merge(arr, start, half, end):
    arr_left = arr[start:half]
    arr_right = arr[half:end]
    j = k = 0
    for i in range(start, end):
        if j == len(arr_left):
            arr[i] = arr_right[k]
            k += 1
        elif k == len(arr_right):
            arr[i] = arr_left[j]
            j += 1
        elif arr_left[j] < arr_right[k]:
            arr[i] = arr_left[j]
            j += 1
        else:
            arr[i] = arr_right[k]
            k += 1


def merge_sort(arr, start, end):
    # if there is only one element to check
    if end == start + 1:
        return

    half = floor((start + end) / 2)
    merge_sort(arr, start, half)
    merge_sort(arr, half, end)
    merge(arr, start, half, end)


a = [1, 56, 43, 2, 33, 67, 12, 435, 355]
merge_sort(a, 0, len(a))
print(a)
