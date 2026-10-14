import pandas as pd

df = pd.read_csv("Student-Performance-Data-Analysis/data/student-mat.csv", sep=";")

#task 01
# Show students with final grades above 15
# high_performers = df[df["G3"] > 15]

# print(high_performers[["sex", "studytime", "G3"]])
# print("Number of high performers:", len(high_performers))

#task 02
# ans = df[(df["G3"] <= 15) & (df["G3"] >= 10)]

# print(ans[["G3", "studytime"]])
# print("Number of students:", len(ans))

#task 03

# x = df['sex'].value_counts()
# print(x)

# gender_avg = df.groupby('sex')['G3'].mean()
# print(gender_avg.sort_values(ascending=False))

# study_avg = df.sort_values('G3',ascending=False)
# print(study_avg[['G3','sex','studytime']].head())

# task 04
# Your code here
# top = df.sort_values('G3' ,ascending = True)
# print(top[['sex','studytime']][:10])

#task 05
no_absence = df[df['absences']==0]['G3'].mean()
with_absence = df[df['absences']>0]['G3'].mean()

print("Zero absences:", no_absence)
print("with absences:", with_absence)