import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

project_dir = Path(__file__).resolve().parents[1]
csv_path = project_dir / "data" / "student-mat.csv"

df = pd.read_csv(csv_path, sep=";")

# Average final grade by study time
result = df.groupby("studytime")["G3"].mean()
#
# plt.figure(figsize=(8, 5))
# plt.bar(result.index, result.values)
# plt.title("Average Final Grade by Study Time")
# plt.xlabel("Study Time (1–4)")
# plt.ylabel("Average Final Grade")
# plt.show()

df["absence_group"] = df["absences"].apply(
    lambda x: "No absences" if x == 0 else "Has absences"
)

result = df.groupby("absence_group")["G3"].mean()

print(result)

print("G1 vs G3:", df["G1"].corr(df["G3"]))
print("G2 vs G3:", df["G2"].corr(df["G3"]))

findings = [
    "G2 has a stronger positive correlation with G3 than G1.",
    "Study time has a weak positive correlation with G3.",
    "Students with absences had a higher average G3 in this dataset.",
    "Correlation does not prove causation."
]

with open("lesson_06_findings.txt", "w") as file:
    for finding in findings:
        file.write(f"- {finding}\n")

print("Findings saved successfully!")