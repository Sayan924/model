# 1. Import library
from sklearn.linear_model import LogisticRegression

# 2. Create data
X = [[1], [2], [3], [4], [5]]   # input
y = [0, 0, 0, 1, 1]             # output (0=Fail, 1=Pass)

# 3. Create model
model = LogisticRegression()

# 4. Train model
model.fit(X, y)

# 5. Test model
prediction = model.predict([[3.5]])
print("Prediction:", prediction)
