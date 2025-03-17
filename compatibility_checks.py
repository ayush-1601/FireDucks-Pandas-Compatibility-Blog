import pandas as pd
import numpy as np

def check_data_type_variation():
    df = pd.DataFrame({"a": [2020, 2021, 2022]})
    result = df["a"] * 2
    print("Pandas Data Type:", result.dtype)

def check_missing_values():
    df = pd.DataFrame({"a": [1.0, np.nan, 3.0]})
    result = df["a"] + 2
    print("\nPandas Missing Value Handling:\n", result)

def check_merge_functionality():
    df1 = pd.DataFrame({"id": [1, 2, 3], "value": ["A", "B", "C"]})
    df2 = pd.DataFrame({"id": [2, 3, 4], "score": [10, 20, 30]})
    
    result = df1.merge(df2, on="id", how="outer")
    print("\nPandas Merge Result:\n", result)

if __name__ == "__main__":
    print("Checking Data Type Variation:")
    check_data_type_variation()

    print("\nChecking Missing Values:")
    check_missing_values()

    print("\nChecking Merge Functionality:")
    check_merge_functionality()