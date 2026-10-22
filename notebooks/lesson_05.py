import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

from pathlib import Path

project_dir = Path(__file__).resolve().parents[1]
csv_path = project_dir / "data" / "student-mat.csv"

df = pd.read_csv(csv_path, sep=";")
#
# plt.figure(figsize=(8, 5))
#
# plt.hist(df["G3"], bins=11, edgecolor="black")
#
# plt.title("Distribution of Final Grades")
# plt.xlabel("Final Grade")
# plt.ylabel("Number of Students")
#
# plt.show()
#
# plt.figure(figsize=(8, 5))
#
# plt.boxplot(df["G3"])
#
# plt.figure(figsize=(8, 5))
#
# plt.scatter(df["studytime"], df["G3"], alpha=0.6)
#
# plt.title("Study Time vs Final Grade")
# plt.xlabel("Study Time")
# plt.ylabel("Final Grade")
#
# plt.show()
#
# plt.title("Distribution of Final Grades")
# plt.ylabel("Final Grade")
#
# plt.show()
#
# avg_grades = df.groupby("studytime")["G3"].mean()
#
# plt.figure(figsize=(8, 5))
# plt.bar(avg_grades.index, avg_grades.values)
# plt.title("Average Final Grade by Study Time")
# plt.xlabel("Study Time")
# plt.ylabel("Average Final Grade")
# plt.show()
#
corr = df[["studytime", "absences", "G1", "G2", "G3"]].corr()
#
# plt.figure(figsize=(8, 6))
# plt.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
# plt.colorbar(label="Correlation")
# plt.xticks(range(len(corr.columns)), corr.columns)
# plt.yticks(range(len(corr.columns)), corr.columns)
# plt.title("Correlation Heatmap")
# plt.show()

print(corr["G3"].sort_values(ascending=False))
