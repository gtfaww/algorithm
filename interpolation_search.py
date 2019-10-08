def binary_search(l, find):
    low = 0
    high = len(l) - 1
    search_count = 0
    while low <= high:
        search_count += 1
        print(search_count)

        mid = int((low + high) / 2)

        if l[mid] == find:
            print("find: {}".format(str(mid)))
            return mid
        elif l[mid] < find:
            low = mid + 1
        elif l[mid] > find:
            high = mid - 1

    return None


def bs(arr, low, high, find):
    if len(arr) < 1:
        return None

    # mid = int((low + high) / 2)
    mid = int(low + (find - arr[low]) / (arr[high] - arr[low]) * (high - low))
    if arr[mid] == find:
        print("find: {}".format(str(mid)))
        return mid
    elif arr[mid] < find:
        low = mid + 1
        bs(arr, low, high, find)
    elif arr[mid] > find:
        high = mid - 1
        bs(arr, low, high, find)


if __name__ == '__main__':
    binary_search(range(10000), 1520)

    bs(range(10000), 0, 9999, 1520)
