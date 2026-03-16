import sys
import random
import time
from dataclasses import dataclass

sys.setrecursionlimit(100000)


# --------------------------------------------------
# Operation Counters (Energy Proxy)
# --------------------------------------------------
@dataclass
class Counters:
    comparisons: int = 0
    assignments: int = 0
    swaps: int = 0

    def reset(self):
        self.comparisons = 0
        self.assignments = 0
        self.swaps = 0


# --------------------------------------------------
# Array Generator
# --------------------------------------------------
def generate_array(n: int, mode: str = "random"):

    if mode == "random":
        arr = [random.randint(0, 10_000_000) for _ in range(n)]

    elif mode == "sorted":
        arr = list(range(n))

    elif mode == "reversed":
        arr = list(range(n, 0, -1))

    elif mode == "nearly_sorted":
        arr = list(range(n))
        for _ in range(max(1, n // 20)):
            i = random.randint(0, n - 1)
            j = random.randint(0, n - 1)
            arr[i], arr[j] = arr[j], arr[i]

    elif mode == "few_unique":
        arr = [random.choice([1,2,3,4,5]) for _ in range(n)]

    else:
        raise ValueError("Unknown mode")

    return arr


# --------------------------------------------------
# Merge Sort
# --------------------------------------------------
def mergesort(arr, counters: Counters):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = mergesort(arr[:mid], counters)
    right = mergesort(arr[mid:], counters)

    return merge(left, right, counters)


def merge(left, right, counters: Counters):

    i = j = 0
    merged = []

    while i < len(left) and j < len(right):

        counters.comparisons += 1

        if left[i] <= right[j]:
            merged.append(left[i])
            counters.assignments += 1
            i += 1
        else:
            merged.append(right[j])
            counters.assignments += 1
            j += 1

    while i < len(left):
        merged.append(left[i])
        counters.assignments += 1
        i += 1

    while j < len(right):
        merged.append(right[j])
        counters.assignments += 1
        j += 1

    return merged


# --------------------------------------------------
# QuickSort (Iterative + Median-of-three Pivot)
# --------------------------------------------------
def quicksort(arr, counters: Counters, low=None, high=None):

    if len(arr) == 0:
        return

    if low is None or high is None:
        low, high = 0, len(arr) - 1

    stack = [(low, high)]

    while stack:

        l, h = stack.pop()

        if l < h:

            p = partition(arr, counters, l, h)

            if p - 1 > l:
                stack.append((l, p - 1))

            if p + 1 < h:
                stack.append((p + 1, h))


def median_of_three(arr, low, high):

    mid = (low + high) // 2
    candidates = [low, mid, high]

    candidates.sort(key=lambda x: arr[x])

    return candidates[1]


def partition(arr, counters: Counters, low, high):

    pivot_index = median_of_three(arr, low, high)

    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    counters.assignments += 3
    counters.swaps += 1

    pivot = arr[high]
    counters.assignments += 1

    i = low - 1

    for j in range(low, high):

        counters.comparisons += 1

        if arr[j] <= pivot:

            i += 1

            arr[i], arr[j] = arr[j], arr[i]

            counters.assignments += 3
            counters.swaps += 1

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    counters.assignments += 3
    counters.swaps += 1

    return i + 1


# --------------------------------------------------
# Test Runner
# --------------------------------------------------
if __name__ == "__main__":

    n = 20

    modes = ["random", "sorted", "reversed", "nearly_sorted", "few_unique"]

    for mode in modes:

        print("\n==============================")
        print("DATA MODE:", mode)

        base_arr = generate_array(n, mode)

        # MergeSort
        c_merge = Counters()
        arr_merge = base_arr.copy()

        start = time.perf_counter()
        sorted_merge = mergesort(arr_merge, c_merge)
        end = time.perf_counter()

        # QuickSort
        c_quick = Counters()
        arr_quick = base_arr.copy()

        start_q = time.perf_counter()
        quicksort(arr_quick, c_quick)
        end_q = time.perf_counter()

        # doğrulama
        assert sorted_merge == sorted(base_arr)
        assert arr_quick == sorted(base_arr)

        print("\nMergeSort")
        print("Time:", end - start)
        print("Comparisons:", c_merge.comparisons)
        print("Assignments:", c_merge.assignments)
        print("Swaps:", c_merge.swaps)

        print("\nQuickSort")
        print("Time:", end_q - start_q)
        print("Comparisons:", c_quick.comparisons)
        print("Assignments:", c_quick.assignments)
        print("Swaps:", c_quick.swaps)