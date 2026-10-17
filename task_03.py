import random
import timeit


def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res


def benchmark():
    sizes = [100, 1000, 5000]

    print(
        f"{'Розмір':<8} | {'Insertion (s)':<15} | {'Merge (s)':<12} | {'Timsort (s)':<12}"
    )
    print("-" * 55)

    for size in sizes:
        data = [random.randint(0, 10000) for _ in range(size)]

        t_ins = timeit.timeit(lambda: insertion_sort(data), number=3) / 3
        t_merge = timeit.timeit(lambda: merge_sort(data), number=3) / 3
        t_tim = timeit.timeit(lambda: sorted(data), number=3) / 3

        print(f"{size:<8} | {t_ins:<15.6f} | {t_merge:<12.6f} | {t_tim:<12.6f}")


if __name__ == "__main__":
    benchmark()

