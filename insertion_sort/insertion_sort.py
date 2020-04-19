def insertion_sort(arr):
    if len(arr) < 2:
        return
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key


arr = [4, 5, 2, 9, 10, 1, 1]
insertion_sort(arr)
print(arr)
