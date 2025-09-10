"""
student_performance_analysis_india_csda.py
Reproducible script to load student_performance_india_with_csda.csv, train models and save outputs.
Requires: pandas, scikit-learn, matplotlib, pickle
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error
import pickle

df = pd.read_csv("student_performance_india_with_csda.csv")
features = ["Hours_Studied_per_week","Attendance_pct","Previous_Score"]
X = df[features]; y = df["Final_Score"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

lr = LinearRegression(); lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
print("Linear Regression - R2:", r2_score(y_test, y_pred_lr), "MAE:", mean_absolute_error(y_test, y_pred_lr))

rf = RandomForestRegressor(n_estimators=150, random_state=42); rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
print("Random Forest - R2:", r2_score(y_test, y_pred_rf), "MAE:", mean_absolute_error(y_test, y_pred_rf))

with open("linear_regression_india_csda.pkl","wb") as f: pickle.dump(lr,f)
with open("random_forest_india_csda.pkl","wb") as f: pickle.dump(rf,f)
