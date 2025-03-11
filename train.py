import json
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt


# def draw_graph(mileage, prices, predicted_prices):
#     plt.title('Linear Regression')
#     plt.xlabel('Mileage (km)')
#     plt.ylabel('Price')
#     plt.scatter(mileage, prices, color='blue', label='Data')
#     plt.plot(mileage, predicted_prices, color='red', label='Regression Line')
#     plt.legend()
#     plt.show()


def perform_gradient_descent(mileage_normalized, prices_normalized, learning_rate, iterations):
    theta0 = 0.0
    theta1 = 0.0
    m = len(mileage_normalized)

    # Gradient descent
    for _ in range(iterations):
        predictions = theta0 + theta1 * mileage_normalized
        errors = predictions - prices_normalized

        # Compute gradients
        tmp_theta0 = learning_rate * (1/m) * np.sum(errors)
        tmp_theta1 = learning_rate * (1/m) * np.sum(errors * mileage_normalized)

        # Update parameters
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    
    return theta0, theta1


def get_mean_std(data):
    data_mean = np.mean(data)
    data_std = np.std(data)
    return data_mean, data_std


def normalize_data(data, data_mean, data_std):
    data_normalized = (data - data_mean) / data_std
    return data_normalized


def save_parameters(denormalized_theta0, denormalized_theta1):
    with open("thetas.json", "w") as file:
        json.dump({"theta0": denormalized_theta0, "theta1": denormalized_theta1}, file)


def get_data_from_file(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)
    
    # Extract mileage and price
    mileage = data['km'].values
    prices = data['price'].values

    return mileage, prices


def main():
    file_path = 'data.csv'

    try:
        # Get data (mileage, prices) from file (data.csv)
        mileage, prices = get_data_from_file(file_path)

        # Initialize parameters
        learning_rate = 0.01
        iterations = 1000

        # Get mean and std
        mileage_mean, mileage_std = get_mean_std(mileage)
        prices_mean, prices_std = get_mean_std(prices)

        # Normalize data (mileage, prices)
        mileage_normalized = normalize_data(mileage, mileage_mean, mileage_std)
        prices_normalized = normalize_data(prices, prices_mean, prices_std)

        # Gradient descent
        theta0, theta1 = perform_gradient_descent(mileage_normalized, prices_normalized, learning_rate, iterations)

        # Denormalize data (theta0, tetha1)
        denormalized_theta0 = prices_mean + (theta0 - theta1 * mileage_mean / mileage_std) * prices_std
        denormalized_theta1 = theta1 * prices_std / mileage_std

        # Save data in file (tetha.json)
        save_parameters(denormalized_theta0, denormalized_theta1)
        print("theta0 =", denormalized_theta0)
        print("theta1 =", denormalized_theta1)

        # Draw graph
        # predicted_prices = denormalized_theta0 + denormalized_theta1 * mileage
        # draw_graph(mileage, prices, predicted_prices)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()