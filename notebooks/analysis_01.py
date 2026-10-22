
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from pathlib import  Path

project_dir = Path(__file__).resolve().parents[1]
csv_path = project_dir / "data" / "student-mat.csv"

df = pd.read_csv(csv_path, sep=";")

df_encoded = df.copy()
for col in df_encoded.select_dtypes(include=['object']).columns:
    df_encoded[col] = df_encoded[col].astype('category').cat.codes


X = df_encoded.drop(columns=['G3', 'G1', 'G2']) 
y = df_encoded['G3']

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)


importance_df = pd.DataFrame({
    'Feature': X.columns,
    'Importance': model.feature_importances_
}).sort_values(by='Importance', ascending=False)


print("Top 10 Most Influential Factors on Student Performance:")
print(importance_df.head(10))

plt.figure(figsize=(10, 6))
plt.barh(importance_df['Feature'].head(10)[::-1], importance_df['Importance'].head(10)[::-1], color='skyblue')
plt.xlabel('Importance Score')
plt.title('Top 10 Factors Influencing Student Final Grades (G3)')
plt.show()