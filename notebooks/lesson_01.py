import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import inspect
df = pd.read_csv("Student-Performance-Data-Analysis/data/student-mat.csv", sep=";")

print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

print("Average:", df["G3"].mean())

print("Highest:", df["G3"].max())
print("Lowest:", df["G3"].min())

print(df.groupby("sex")["G3"].mean())

grades = df["G3"].to_numpy()
print("NumPy average:", np.mean(grades))

# Calculate the median final grade.
print('median final',np.median(grades))


# Count how many students scored 15 or higher.
print('student >15 score:',np.count_nonzero(grades[grades>=15]))


# Find the average final grade for students who studied more (studytime == 4).
print('av final studytime >4',df.loc[df['studytime']==4,"G3"].mean())

# plt.hist(df["G3"], bins=10)

# ds = df.groupby('sex')['G3'].mean()
# plt.bar(ds.index,ds.values)
# plt.title("Distribution of Final Grades mean by gender")
# plt.xlabel("sex")
# plt.ylabel("distribution by gender")
# plt.show()

# plt.scatter(df["G2"], df["G3"],alpha=0.5)

# plt.title("Second Period vs Final Grades")
# plt.grid(True)
# plt.xlabel("G2 Grade")
# plt.ylabel("G3 Grade")
# plt.show()

# plt.figure(figsize=(8, 5))

study_grades = df.groupby("studytime")["G3"].mean()

# plt.figure(figsize=(8, 5))
# plt.bar(study_grades.index, study_grades)
# plt.title("Study Time vs Average Final Grade")
# plt.xlabel("Study Time")
# plt.ylabel("Average Final Grade")
# plt.show()

# plt.figure(figsize=(8, 5))
# plt.plot(study_grades.index, study_grades, marker="o")
# plt.title("Study Time vs Average Final Grade")
# plt.xlabel("Study Time (1 = Lowest, 4 = Highest)")
# plt.ylabel("Average Final Grade")
# plt.grid(True)
# plt.show()

# plt.figure(figsize=(8, 5))
# plt.scatter(df["absences"], df["G3"], alpha=0.5)
# plt.title("Absences vs Final Grades")
# plt.xlabel("Number of Absences")
# plt.ylabel("Final Grade")
# plt.grid(True)
# plt.show()

# correlation = df["absences"].corr(df["G3"])
# print(correlation)

print("G1:", df["G1"].corr(df["G3"]))
print("G2:", df["G2"].corr(df["G3"]))
print("Absences:", df["absences"].corr(df["G3"]))