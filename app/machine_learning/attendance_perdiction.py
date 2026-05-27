from sklearn.linear_model import LinearRegression
import numpy as np

def predict():

    x = np.array([[1], [2], [3]])
    y = np.array([80, 85, 90])

    model = LinearRegression()
    model.fit(x, y)

    result = model.predict([[4]])

    return result