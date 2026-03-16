# Divide & Conquer Energy Project

This project compares two Divide & Conquer sorting algorithms: **MergeSort** and **QuickSort**.  
The goal is to analyze their performance not only in terms of runtime but also by counting the operations performed during execution. These operation counts are used to estimate an approximate **energy proxy metric**. The project also includes a **Streamlit GUI**, which allows experiments to be run interactively.

## Purpose

The main purpose of this project is to compare MergeSort and QuickSort under different input conditions and analyze how their behavior changes. The following metrics are measured during the experiments:

- **Execution time (avg_time_ms)** – how long the algorithm takes to run.
- **Number of comparisons (avg_comp)** – how many comparisons the algorithm performs.
- **Number of assignments / swaps (avg_assign)** – how many data movements occur.
- **Energy proxy metric** – an approximate measure of computational work.

The energy proxy is calculated using the following formula:

energy_proxy = comparisons + assignments

*Note:* This value is **not a real measurement of electrical energy**. It is only an approximate indicator of how much work the algorithm performs. The project can also optionally estimate energy consumption and carbon emissions using the **CodeCarbon** library. CodeCarbon does not directly measure hardware power usage; it provides estimated values.

## Experiment Scenarios

To better observe algorithm behavior, the experiments are performed using three different dataset types:

- **random** – randomly generated data (represents average-case conditions)
- **sorted** – already sorted data (used to observe special-case behavior)
- **reversed** – reverse sorted data (used as a stress test and near worst-case scenario)

Testing with different data patterns helps demonstrate how algorithms react to different input conditions.

## Project Structure

The project contains three main Python files:

- **algorithms.py**  
  Implements MergeSort and an **iterative QuickSort** algorithm.  
  It also contains operation counters and a dataset generator.

- **benchmark.py**  
  Runs experiments using different input sizes and dataset modes.  
  It measures runtime, operation counts, and energy proxy values, then prints the results in a table.

- **gui_app.py**  
  Provides a **Streamlit-based graphical interface**.  
  Users can select parameters such as dataset size, data mode, and number of repetitions, then visualize the results with graphs.

## Installation and Running

Follow these steps to run the project.

### 1. Open the terminal and go to the project directory

cd /Users/your_username/Desktop/divide-and-conquer-energy-project

*(Navigate to the folder where the project files are located.)*

### 2. Create and activate a virtual environment (recommended)

python3 -m venv .venv  
source .venv/bin/activate

*(This keeps project dependencies isolated from other Python projects.)*

### 3. Install the required libraries

python -m pip install --upgrade pip  
python -m pip install streamlit pandas codecarbon

*(These libraries are used for the GUI, data handling, and energy estimation.)*

If a requirements file exists, you can alternatively run:

python -m pip install -r requirements.txt

### 4. Run the Streamlit GUI

streamlit run gui_app.py

*(This starts the graphical interface where experiments can be run interactively.)*

After running the command, open the following address in your browser:

http://localhost:8501

Press **Ctrl+C** in the terminal to stop the application.

### 5. Run a quick algorithm test (terminal output only)

python algorithms.py

*(This runs a small test to verify that the sorting algorithms work correctly.)*

### 6. Run the full benchmark experiments

python benchmark.py

*(This executes all experiments and prints the results in the terminal.)*

## Quick Fix: CodeCarbon Error

If you encounter the following error while running the GUI:

ModuleNotFoundError: codecarbon

run the following commands:

source .venv/bin/activate  
python -m pip install --upgrade pip  
python -m pip install codecarbon  
streamlit run gui_app.py

*(This installs the missing library and restarts the GUI.)*

## Author

**Leyla Erdemir**  
Software Engineering Student
