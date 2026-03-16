import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from benchmark import run_experiment

st.set_page_config(page_title="Sorting Algorithm Energy Analysis", layout="wide")

st.title("Sorting Algorithm Energy Analysis")
st.write("Comparison of MergeSort and QuickSort based on runtime and operation metrics")

# Sidebar settings
st.sidebar.header("Experiment Settings")

n = st.sidebar.selectbox("Array Size", [100, 500, 1000, 2000, 5000], index=2)
mode = st.sidebar.selectbox("Dataset Type", ["random", "sorted", "reversed"])
repetitions = st.sidebar.slider("Repetitions", 1, 10, 5)

run = st.button("Run Experiment")

if run:

    merge_res, quick_res = run_experiment(n, mode, repetitions)

    st.success("Experiment completed")

    # DataFrame
    df = pd.DataFrame([merge_res, quick_res])

    # Results Table
    st.subheader("Results Table")
    st.dataframe(df)

    # Key Metrics
    st.subheader("Key Metrics")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("MergeSort Runtime", f"{merge_res['time']:.3f} ms")
        st.metric("MergeSort Energy Proxy", f"{merge_res['energy']:.1f}")

    with col2:
        st.metric("QuickSort Runtime", f"{quick_res['time']:.3f} ms")
        st.metric("QuickSort Energy Proxy", f"{quick_res['energy']:.1f}")

    # Runtime Comparison Graph
    st.subheader("Runtime Comparison")

    fig, ax = plt.subplots(figsize=(6,4))

    algorithms = ["MergeSort", "QuickSort"]
    runtimes = [merge_res["time"], quick_res["time"]]

    ax.bar(algorithms, runtimes, width=0.4, color=["#4C72B0", "#DD8452"])

    ax.set_title("MergeSort vs QuickSort Runtime")
    ax.set_ylabel("Runtime (ms)")
    ax.grid(axis="y")

    st.pyplot(fig)

    # Energy Comparison Graph
    st.subheader("Energy Comparison")

    fig2, ax2 = plt.subplots(figsize=(6,4))

    energies = [merge_res["energy"], quick_res["energy"]]

    ax2.bar(algorithms, runtimes, width=0.4, color=["#4C72B0", "#DD8452"])

    ax2.set_title("MergeSort vs QuickSort Energy Proxy")
    ax2.set_ylabel("Energy")
    ax2.grid(axis="y")

    st.pyplot(fig2)