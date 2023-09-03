# Exploring different sort methods with user input sort_fn
# Initialize a global counter to keep track of comparisons
comparison_count = 0


def quick_sort(arr, sort_fn):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if sort_fn(x, pivot)]
    right = [x for x in arr[1:] if not sort_fn(x, pivot)]
    print(left, right)

    return quick_sort(left, sort_fn) + [pivot] + quick_sort(right, sort_fn)


def merge_sort(arr, sort_fn):
    print(arr)
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left, sort_fn)
    right = merge_sort(right, sort_fn)

    return merge(left, right, sort_fn)


def merge(left, right, sort_fn):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if sort_fn(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


def heapify(arr, n, i, sort_fn):
    print(arr)
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and sort_fn(arr[left], arr[smallest]):
        smallest = left

    if right < n and sort_fn(arr[right], arr[smallest]):
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest, sort_fn)


def heap_sort(arr, sort_fn):
    n = len(arr)

    # Build a min heap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, sort_fn)

    # Extract elements one by one to build a sorted array.
    sorted_arr = [0] * n
    for i in range(n):
        sorted_arr[n - 1 - i] = arr[0]
        arr[0] = arr[n - 1 - i]
        heapify(arr, n - 1 - i, 0, sort_fn)

    return sorted_arr



def user_choice(L, R):
    global comparison_count  # Access the global counter
    user_input = input(f"[1] {L} vs [2] {R}: ").strip().lower()
    comparison_count += 1
    return str(user_input) == str(1)


if __name__ == "__main__":
    comparison_count = 0
    # Example usage:
    # arr = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    arr = ["C", "B", "D", "A", "F", "H", "G", "E", "I"]
    # sorted_list = merge_sort(unsorted_list, user_choice)
    # print(sorted_list)

    print("Original array:", arr)
    # result = merge_sort(arr, user_choice)
    result = heap_sort(arr, user_choice)
    print("Sorted array:", result)
    print('Comparison count:', comparison_count)
