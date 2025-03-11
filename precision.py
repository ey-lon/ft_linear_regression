import json
import numpy as np
import pandas as pd


def get_data_from_file(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)
    
    # Extract mileage and price
    mileage = data['km'].values
    prices = data['price'].values

    return mileage, prices


def get_thetas_from_file(file_path):
    with open(file_path, "r") as file:
        thetas = json.load(file)
    theta0 = float(thetas["theta0"])
    theta1 = float(thetas["theta1"])

    return theta0, theta1


def calculate_precision(predicted_prices, prices):
    # Calculate precision metrics
    errors = prices - predicted_prices

    # Mean Squared Error
    mse = np.mean(errors ** 2)

    # Mean Absolute Error
    mae = np.mean(np.abs(errors))

    # R-squared
    ss_residual = np.sum(errors ** 2)
    ss_total = np.sum((prices - np.mean(prices)) ** 2)
    r_squared = 1 - (ss_residual / ss_total)

    # Display precision metrics
    print(f"Mean Squared Error (MSE): {mse:.2f}")
    print(f"Mean Absolute Error (MAE): {mae:.2f}")
    print(f"R-squared (R²): {r_squared:.2f}")


def main():
    data_path = "data.csv"
    parameters_file = "thetas.json"

    try:
        # Load the parameters saved from the training program
        theta0, theta1 = get_thetas_from_file(parameters_file)
        mileage, prices = get_data_from_file(data_path)

        predicted_prices = theta0 + theta1 * mileage
        calculate_precision(predicted_prices, prices)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
