import pandas as pd
import numpy as np

df = pd.read_csv("Student-Performance-Data-Analysis/data/student-mat.csv", sep=";")

# task 01
#to_numpy() converts a Pandas column into a NumPy array.

grades = df["G3"].to_numpy()

# print("Mean:", np.mean(grades))
# print("Median:", np.median(grades))
# print("Highest:", np.max(grades))
# print("Lowest:", np.min(grades))
# print("Standard deviation:", np.std(grades))
# count = np.sum(grades <=10)
# count2 = np.count_nonzero(grades<=10)
# print(count,count2)

# abv_15 = np.count_nonzero(grades>15)
# print((abv_15/len(grades)*100))

# #task 02
# unique_grades, counts = np.unique(grades, return_counts=True)

# most_common = unique_grades[np.argmax(counts)]

# print("Most common grade:", most_common)
# print("Number of students:", counts.max())


# # task 03
# percentages = counts / len(grades) * 100
# print(percentages[:5])

# for grade, percentage in zip(unique_grades[:5], percentages[:5]):
#     print(f"Grade {grade}: {percentage:.2f}%")

# below_10 = np.mean(grades<=10)*100
# print(below_10)
# above_mean = np.mean(grades > np.mean(grades)) * 100
# print(above_mean)
