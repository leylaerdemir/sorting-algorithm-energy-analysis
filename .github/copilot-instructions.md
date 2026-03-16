# Repository guide for AI coding agents

This small project compares MergeSort and QuickSort using operation counters as a proxy energy metric. The instructions below capture the essential architecture, developer workflows, and code patterns that are discoverable in the repo so an AI agent can be productive quickly.

Key files
- `algorithms.py` — algorithm implementations and `Counters` dataclass (comparisons, assignments, swaps). See `generate_array(...)` for dataset modes: `random`, `sorted`, `reversed`, `nearly_sorted`, `few_unique`.
- `benchmark.py` — harness that runs `mergesort` and `quicksort` via `run_algorithm(algorithm, array)` and `run_experiment(n, mode, repetitions)` returning averaged dicts.
- `gui_app.py` — Streamlit frontend that calls `benchmark.run_experiment` and expects results as plain dicts with keys like `time`, `comparisons`, `assignments`, `energy`.
- `README.MD` — contains setup and run commands (venv, pip install, `streamlit run gui_app.py`) and a troubleshooting note for `codecarbon` import errors.
- `powermetrics_log.txt` — raw power sample logs; present for reference (not consumed by code).

Big-picture architecture & data flow (short)
- Data generation: `generate_array(n, mode)` in `algorithms.py` produces an input array.
- Measurement: `benchmark.run_algorithm` creates a `Counters()` instance, copies the array, executes the algorithm and measures time with `time.perf_counter()`.
- Aggregation: `run_experiment` runs both algorithms multiple times and returns averaged result dicts for each algorithm. `gui_app.py` consumes those dicts to render tables and plots.

Important code patterns and conventions
- Counters object is passed into algorithms and mutated in-place. Code expects fields: `comparisons`, `assignments`, `swaps`. Energy proxy = comparisons + assignments (`energy` key in benchmark results).
- `mergesort` returns a new sorted list; `quicksort` sorts in-place and returns None. `benchmark.run_algorithm` calls algorithms uniformly as `algorithm(arr, metrics)` — both functions accept (array, counters) even if `mergesort` returns a value.
- QuickSort is implemented iteratively using an explicit stack and uses a median-of-three pivot chosen by `median_of_three(arr, low, high)`.
- Dataset `mode` strings are the canonical names used across the repo (`random`, `sorted`, `reversed`, `nearly_sorted`, `few_unique`). Use those exact strings when wiring tests or GUI options.

Developer workflows & runtime commands (verified in README)
- Create and activate virtualenv: `python3 -m venv .venv && source .venv/bin/activate` (macOS zsh).
- Install dependencies: `python -m pip install streamlit pandas codecarbon matplotlib` (or `-r requirements.txt` if added).
- Run GUI: `streamlit run gui_app.py` (opens at http://localhost:8501).
- Quick CLI runs: `python algorithms.py` or `python benchmark.py` to run tests/benchmarks from terminal.

Project-specific gotchas & debugging
- `algorithms.py` uses recursion for `mergesort` and sets `sys.setrecursionlimit(100000)`; large `n` may still be heavy on memory/stack depth.
- `quicksort` is in-place; tests/assertions in `algorithms.py` rely on `arr_quick` being sorted after calling `quicksort`.
- `codecarbon` is optional and mentioned in README; if it's not installed the GUI may still run but some optional metrics will be missing. The README contains the precise fix for `ModuleNotFoundError: codecarbon`.

Examples & data shapes (copy/paste friendly)
- Counters dataclass fields: `{comparisons:int, assignments:int, swaps:int}`
- run_experiment signature: `run_experiment(n:int, mode:str, repetitions:int=5) -> (merge_avg:dict, quick_avg:dict)`
- Result dict example keys: `{'algo','n','mode','time','comparisons','assignments','energy'}`

When making changes
- Preserve the public function signatures used by the GUI: `benchmark.run_experiment(...)` and `run_algorithm(algorithm, array)` must stay compatible with `gui_app.py` unless you update the GUI.
- If you change `generate_array` modes, update `gui_app.py` selectbox options and README strings accordingly.

Where to look next (for feature work or bug fixes)
- Start at `benchmark.run_algorithm` to add additional metrics (e.g., return `swaps` or CodeCarbon values). Update `gui_app.py` to render any new keys.
- Inspect `algorithms.py` to modify operation-count logic — counters are incremented inline near comparisons/assignments.

If anything in this file is unclear or you'd like me to expand a section (tests, CI config, or example unit tests), tell me which area to elaborate and I'll update this file.
