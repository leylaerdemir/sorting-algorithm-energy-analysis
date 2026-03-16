import time

# Import sorting algorithms and operation counter from algorithms.py
from algorithms import Counters, generate_array, mergesort, quicksort


def run_algorithm(algorithm, array):
    """
    Executes a sorting algorithm and returns performance metrics.

    Returned metrics:
    - execution time (milliseconds)
    - number of comparisons
    - number of assignments
    - energy proxy (comparisons + assignments)
    """

    # Create counter object to track algorithm operations
    metrics = Counters()

    # Copy array so original data is not modified
    arr = array.copy()

    # Measure execution time
    start = time.perf_counter()
    algorithm(arr, metrics)
    end = time.perf_counter()

    # Convert runtime to milliseconds
    runtime_ms = (end - start) * 1000

    return {
        "time": runtime_ms,
        "comparisons": metrics.comparisons,
        "assignments": metrics.assignments,
        "energy_proxy": metrics.comparisons + metrics.assignments
    }


def run_experiment(n, mode, repetitions=5):
    """
    Runs MergeSort and QuickSort multiple times
    for a given dataset size and scenario.

    Returns average results.
    """

    merge_results = []
    quick_results = []

    # Run the experiment multiple times for stable averages
    for _ in range(repetitions):

        # Generate test dataset
        base_array = generate_array(n, mode)

        # Measure MergeSort performance
        merge_results.append(run_algorithm(mergesort, base_array))

        # Measure QuickSort performance
        quick_results.append(run_algorithm(quicksort, base_array))

    # Helper function to compute averages
    def average(results, key):
        return sum(r[key] for r in results) / len(results)

    # Average results for MergeSort
    merge_avg = {
        "algo": "MergeSort",
        "n": n,
        "mode": mode,
        "time": average(merge_results, "time"),
        "comparisons": average(merge_results, "comparisons"),
        "assignments": average(merge_results, "assignments"),
        "energy": average(merge_results, "energy_proxy")
    }

    # Average results for QuickSort
    quick_avg = {
        "algo": "QuickSort",
        "n": n,
        "mode": mode,
        "time": average(quick_results, "time"),
        "comparisons": average(quick_results, "comparisons"),
        "assignments": average(quick_results, "assignments"),
        "energy": average(quick_results, "energy_proxy")
    }

    return merge_avg, quick_avg


def print_result(result):
    """
    Prints algorithm results in table format.
    """

    print(
        f"{result['algo']:<10} "
        f"{result['n']:>8} "
        f"{result['mode']:>10} "
        f"{result['time']:>12.3f} ms "
        f"{result['comparisons']:>12.1f} "
        f"{result['assignments']:>12.1f} "
        f"{result['energy']:>12.1f}"
    )


def run_all_experiments():
    """
    Executes benchmark experiments for different
    input sizes and dataset scenarios.
    """

    # Input sizes for the benchmark
    sizes = [1000, 5000, 10000]

    # Dataset patterns
    modes = ["random", "sorted", "reversed"]

    print("\n=== Sorting Benchmark ===\n")

    # Table header
    print(f"{'Algo':<10} {'n':>8} {'mode':>10} {'time':>15} {'comp':>12} {'assign':>12} {'energy':>12}")
    print("-" * 80)

    for n in sizes:
        for mode in modes:

            merge_res, quick_res = run_experiment(n, mode)

            print_result(merge_res)
            print_result(quick_res)

        print("-" * 80)


# Run benchmark when file is executed directly
if __name__ == "__main__":
    run_all_experiments()