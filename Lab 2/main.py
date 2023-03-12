import random
import time
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(10000)


# Function to generate arrays of different orders and sizes
def generate_random_array(n, lower, upper):
    arr = [random.randint(lower, upper) for _ in range(n)]
    return arr


# Function to measure the execution time and memory usage of a function
def measure(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    memory_usage = 0  # TODO: measure memory usage
    return end_time - start_time, memory_usage


# Sorting algorithms
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    stack = [(0, len(arr) - 1)]
    while stack:
        left, right = stack.pop()
        if left >= right:
            continue
        pivot = arr[(left + right) // 2]
        i, j = left, right
        while i <= j:
            while arr[i] < pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        if j > left:
            stack.append((left, j))
        if i < right:
            stack.append((i, right))
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged


def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr


def bogo_sort(arr):
    n=0
    while not is_sorted(arr):
        random.shuffle(arr)
        n = n+1
        print(n)
    return arr


def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


metrics = {
    'time': {},
    'memory': {},
}


def time_execution(algorithm, arr):
    start = time.time()
    algorithm(arr)
    end = time.time()
    return end - start


def print_for_plot():
    plt.xlabel('Input size')
    plt.ylabel('Execution time (seconds)')
    plt.legend()
    plt.show()


def plot_results(n_values, time_values, title, label):
    plt.plot(n_values, time_values, label=label)
    plt.title(title)
    print_for_plot()


def plot_all_results(n_values, time_values_quick, time_values_merge, time_values_heap, time_values_bogo):
    plt.plot(n_values, time_values_quick, label='Quick sort')
    plt.plot(n_values, time_values_merge, label='Merge sort')
    plt.plot(n_values, time_values_heap, label='Heap sort')
    plt.plot(n_values, time_values_bogo, label='Bogo sort')
    print_for_plot()


def plot_qs_ms_hs(n_values, time_values_quick, time_values_merge, time_values_heap):
    plt.plot(n_values, time_values_quick, label='Quick sort')
    plt.plot(n_values, time_values_merge, label='Merge sort')
    plt.plot(n_values, time_values_heap, label='Heap sort')
    print_for_plot()


def print_array(arr):
    print("[", end="")
    for i in range(len(arr)):
        if i != len(arr) - 1:
            print(arr[i], end=", ")
        else:
            print(arr[i], end="")
    print("]")


if __name__ == '__main__':
    # Set up variables for testing
    n_values = [5,6,7,8,9,10]
    lower = 0
    upper = 100000

    # Generate random arrays for testing
    array = [generate_random_array(n, lower, upper) for n in n_values]

    unsorted_arr_for_q = array.copy()
    unsorted_arr_for_m = array.copy()
    unsorted_arr_for_h = array.copy()
    unsorted_arr_for_b = array.copy()

    # Test each algorithm on each array and record execution time
    quick_sort_times = []
    merge_sort_times = []
    heap_sort_times = []
    bogo_sort_times = []

    for arr in unsorted_arr_for_b:
        bogo_sort_times.append(time_execution(bogo_sort, arr))

    for arr in unsorted_arr_for_q:
        quick_sort_times.append(time_execution(quick_sort, arr))

    for arr in unsorted_arr_for_m:
        merge_sort_times.append(time_execution(merge_sort, arr))

    for arr in unsorted_arr_for_h:
        heap_sort_times.append(time_execution(heap_sort, arr))


    print("Quick sort")
    for arr in unsorted_arr_for_q:
        print_array(quick_sort(arr))

    print("Merge sort")
    for arr in unsorted_arr_for_m:
        print_array(merge_sort(arr))

    print("Heap sort")
    for arr in unsorted_arr_for_h:
        print_array(heap_sort(arr))

    print("Bogo sort")
    for arr in unsorted_arr_for_b:

        print_array(bogo_sort(arr))

    # Plot the results
    plot_results(n_values, quick_sort_times, 'Quick sort', 'Quick sort')
    plot_results(n_values, merge_sort_times, 'Merge sort', 'Merge sort')
    plot_results(n_values, heap_sort_times, 'Heap sort', 'Heap sort')
    plot_results(n_values, bogo_sort_times, 'Bogo sort', 'Bogo sort')

    plot_all_results(n_values, quick_sort_times, merge_sort_times, heap_sort_times, bogo_sort_times)

    n_values = [10000, 100000, 1000000]
    lower = 0
    upper = 1000000

    array = [generate_random_array(n, lower, upper) for n in n_values]

    unsorted_arr_for_q = array.copy()
    unsorted_arr_for_m = array.copy()
    unsorted_arr_for_h = array.copy()

    quick_sort_times = []
    merge_sort_times = []
    heap_sort_times = []

    for arr in unsorted_arr_for_q:
        quick_sort_times.append(time_execution(quick_sort, arr))

    for arr in unsorted_arr_for_m:
        merge_sort_times.append(time_execution(merge_sort, arr))

    for arr in unsorted_arr_for_h:
        heap_sort_times.append(time_execution(heap_sort, arr))

    plot_qs_ms_hs(n_values, quick_sort_times, merge_sort_times, heap_sort_times)



