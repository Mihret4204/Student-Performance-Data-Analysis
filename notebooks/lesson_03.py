import pandas as pd
import numpy as np
df = pd.read_csv("Student-Performance-Data-Analysis/data/student-mat.csv", sep=";")

# task 001
# print(df.isnull().sum())

# data = pd.Series([10, 15, np.nan, 20, np.nan, 25])

# print("Original data:")
# print(data)
#task 02
# print("Missing values:", data.isnull().sum())

# clean_data = data.dropna()
# print("Cleaned data:")
# print(clean_data)
#task 03
# data = pd.Series([10, 15, np.nan, 20, np.nan, 25])

# filled_data = data.fillna(data.mean())

# print(filled_data)

# task 04

# data = pd.Series([10, 20, 20, 30, 30, 30, 40])

# print(data.drop_duplicates())

# task 05
# data = pd.DataFrame({
#     "name": ["Abel", "Sara", "Abel", "Miki"],
#     "grade": [15, 18, 15, 12]
# })

# print(data.duplicated())
# cleaned_data = data.drop_duplicates()
# print(cleaned_data)
# print("Duplicate rows:", df.duplicated().sum())
# print(df.dtypes)

#task 06
print(df.dtypes.value_counts())