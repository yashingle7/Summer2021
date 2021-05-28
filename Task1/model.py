import numpy
import pandas
import joblib

data = pandas.read_csv('SalaryData.csv')
X=data['YearsExperience'].values.reshape(-1,1)
y=data['Salary']
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X,y)
joblib.dump(model, 'salary_prediction_app.pk1')
