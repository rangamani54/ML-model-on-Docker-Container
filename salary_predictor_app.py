import joblib
model = joblib.load('salary_predictor.pkl')
p = input("Enter the experience of employe: ")
output = model.predict([[int(p)]])
print(output)

