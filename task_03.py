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
        f"{'Порівняння':<15} | {'Розмір':<8} | {'Insertion (s)':<15} | {'Merge (s)':<12} | {'Timsort (s)':<12}"
    )
    print("-" * 75)

    for size in sizes:
        random_data = [random.randint(0, 100000) for _ in range(size)]
        sorted_data = sorted(random_data)
        reversed_data = list(reversed(sorted_data))

        t_ins_random = timeit.timeit(lambda: insertion_sort(random_data), number=3) / 3
        t_ins_sorted = timeit.timeit(lambda: insertion_sort(sorted_data), number=3) / 3
        t_ins_reversed = timeit.timeit(lambda: insertion_sort(reversed_data), number=3) / 3

        t_merge_random = timeit.timeit(lambda: merge_sort(random_data), number=3) / 3
        t_merge_sorted = timeit.timeit(lambda: merge_sort(sorted_data), number=3) / 3
        t_merge_reversed = timeit.timeit(lambda: merge_sort(reversed_data), number=3) / 3

        t_tim_random = timeit.timeit(lambda: sorted(random_data), number=3) / 3
        t_tim_sorted = timeit.timeit(lambda: sorted(sorted_data), number=3) / 3
        t_tim_reversed = timeit.timeit(lambda: sorted(reversed_data), number=3) / 3

        print(f"{'Випадковий':<15} | {size:<8} | {t_ins_random:<15.6f} | {t_merge_random:<12.6f} | {t_tim_random:<12.6f}")
        print(f"{'Відсортований':<15} | {size:<8} | {t_ins_sorted:<15.6f} | {t_merge_sorted:<12.6f} | {t_tim_sorted:<12.6f}")
        print(f"{'Зворотний':<15} | {size:<8} | {t_ins_reversed:<15.6f} | {t_merge_reversed:<12.6f} | {t_tim_reversed:<12.6f}")


if __name__ == "__main__":
    benchmark()

