def selection_sort(arr):
    for i in range(len(arr) - 1):
        smallest = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest]:
                smallest = j
        if smallest != i:
            holder = arr[i]
            arr[i] = arr[smallest]
            arr[smallest] = holder

a = [1, 32,5,67,23,3,5, -1]
selection_sort(a)
print(a)