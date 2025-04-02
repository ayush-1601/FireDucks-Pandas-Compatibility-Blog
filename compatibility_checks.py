import pandas as pd
import numpy as np

try:
    import cudf
    use_gpu = True
except ImportError:
    use_gpu = False

try:
    from fireducks.core import get_fireducks_options
    import fireducks as fd
    use_fireducks = True

    # Enable FireDucks benchmarking mode
    get_fireducks_options().set_benchmark_mode(True)
except ImportError:
    use_fireducks = False

def evaluate(df):
    """Force evaluation in FireDucks to ensure accurate results."""
    try:
        df._evaluate()
    except AttributeError:
        pass

def check_data_type_variation():
    df = pd.DataFrame({"a": [2020, 2021, 2022]})
    result = df["a"] * 2
    print("Pandas Data Type:", result.dtype)

    if use_gpu:
        gdf = cudf.DataFrame({"a": [2020, 2021, 2022]})
        gpu_result = gdf["a"] * 2
        print("cuDF Data Type:", gpu_result.dtype)

    if use_fireducks:
        fdf = fd.DataFrame({"a": [2020, 2021, 2022]})
        fd_result = fdf["a"] * 2
        evaluate(fd_result)
        print("FireDucks Data Type:", fd_result.dtype)

def check_missing_values():
    df = pd.DataFrame({"a": [1.0, np.nan, 3.0]})
    result = df["a"] + 2
    print("\nPandas Missing Value Handling:\n", result)

    if use_gpu:
        gdf = cudf.DataFrame({"a": [1.0, None, 3.0]})
        gpu_result = gdf["a"] + 2
        print("\ncuDF Missing Value Handling:\n", gpu_result)

    if use_fireducks:
        fdf = fd.DataFrame({"a": [1.0, None, 3.0]})
        fd_result = fdf["a"] + 2
        evaluate(fd_result)
        print("\nFireDucks Missing Value Handling:\n", fd_result)

def check_merge_functionality():
    df1 = pd.DataFrame({"id": [1, 2, 3], "value": ["A", "B", "C"]})
    df2 = pd.DataFrame({"id": [2, 3, 4], "score": [10, 20, 30]})
    
    result = df1.merge(df2, on="id", how="outer")
    print("\nPandas Merge Result:\n", result)

    if use_gpu:
        gdf1 = cudf.DataFrame({"id": [1, 2, 3], "value": ["A", "B", "C"]})
        gdf2 = cudf.DataFrame({"id": [2, 3, 4], "score": [10, 20, 30]})
        gpu_result = gdf1.merge(gdf2, on="id", how="outer")
        print("\ncuDF Merge Result:\n", gpu_result)

    if use_fireducks:
        fdf1 = fd.DataFrame({"id": [1, 2, 3], "value": ["A", "B", "C"]})
        fdf2 = fd.DataFrame({"id": [2, 3, 4], "score": [10, 20, 30]})
        fd_result = fdf1.merge(fdf2, on="id", how="outer")
        evaluate(fd_result)
        print("\nFireDucks Merge Result:\n", fd_result)

if __name__ == "__main__":
    print("Checking Data Type Variation:")
    check_data_type_variation()

    print("\nChecking Missing Values:")
    check_missing_values()

    print("\nChecking Merge Functionality:")
    check_merge_functionality()
