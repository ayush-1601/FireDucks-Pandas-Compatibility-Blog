# FireDucks Pandas Compatibility

This repository demonstrates how **FireDucks** ensures seamless compatibility between **pandas** and **cuDF** in GPU-based data processing.  
It addresses key challenges such as:
- **Data Type Variations**: Aligning pandas' `int64` with cuDF's `int32` to prevent overflow.
- **Missing Value Handling**: Standardizing `NaN` in pandas and `<NA>` in cuDF.
- **Merge Functionality Differences**: Ensuring consistency in `merge()` results.

---

## 🚀 Features
- ✅ Handles pandas-cuDF **data type mismatches**  
- ✅ Standardizes **missing value propagation**  
- ✅ Ensures **consistent merge results**  
- ✅ Supports **both CPU (pandas) & GPU (cuDF)** processing  

---

## Usage
Run the script to compare pandas and cuDF behavior:
```bash
python compatibility_checks.py
