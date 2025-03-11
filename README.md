# ft_linear_regression
An introduction to machine learning consisting in a program that predicts the price of a car by using a linear function train with a gradient descent algorithm.

## How to use:

### - Train:
Calculate theta0 and theta1, given the data (mileage and prices) in data.csv.
```shell
python3 train.py
```

### - Predict:
Predict the price, given the data (theta0 and theta1) in thetas.json and the mileage(km) passed as input.
```shell
python3 predict.py
```

### - Show graph:
Plotting the data and the line resulting from the linear regression into a graph.
```shell
python3 graph.py
```

### - Calculate precision:
Display precision metrics:
- Mean Squared Error (MSE)
- Mean Absolute Error (MAE)
- R-squared (R²)
```shell
python3 precision.py
```
