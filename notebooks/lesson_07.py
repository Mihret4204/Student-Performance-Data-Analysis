import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import  Path

project_dir = Path(__file__).resolve().parents[1]
csv_path = project_dir / "data" / "student-mat.csv"

df = pd.read_csv(csv_path, sep=";")
print(df.head())

av_t = df.groupby("studytime")["G3"].mean()

plt.figure(figsize=(8, 5))
plt.bar(av_t.index, av_t.values)

plt.title("Average Final Grade by Study Time")
plt.xlabel("Study Time")
plt.ylabel("Average Final Grade (G3)")
plt.xticks([1, 2, 3, 4])
plt.show()


print("Correlation:", df["studytime"].corr(df["G3"]))
print(av_t)
so_find = "we can see no direct correlation between study time and final grade"

print(so_find)