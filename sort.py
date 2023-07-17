# Exploring different sort methods with user input sort_fn

def quick_sort(arr, sort_fn):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if sort_fn(x, pivot)]
    right = [x for x in arr[1:] if not sort_fn(x, pivot)]
    print(left, right)

    return quick_sort(left, sort_fn) + [pivot] + quick_sort(right, sort_fn)


def merge_sort(arr, sort_fn):
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


def user_choice(L, R):
    user_input = input(f"[1] {L} vs [2] {R}: ").strip().lower()
    return str(user_input) == str(1)


if __name__ == '__main__':
    # Example usage:
    unsorted_list = ['brown', 'fox', 'the', 'a', 'jumped', 'lazy', 'quick', 'dogs', 'over']
    sorted_list = merge_sort(unsorted_list, user_choice)
    print(sorted_list)