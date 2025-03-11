import json
import pandas as pd
import matplotlib.pyplot as plt


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


def draw_graph(mileage, prices, predicted_prices):
    plt.title('Linear Regression')
    plt.xlabel('Mileage (km)')
    plt.ylabel('Price')
    plt.scatter(mileage, prices, color='blue', label='Data')
    plt.plot(mileage, predicted_prices, color='red', label='Regression Line')
    plt.legend()
    plt.show()


def main():
    data_path = "data.csv"
    parameters_file = "thetas.json"

    try:
        # Load the parameters saved from the training program
        theta0, theta1 = get_thetas_from_file(parameters_file)
        mileage, prices = get_data_from_file(data_path)

        predicted_prices = theta0 + theta1 * mileage
        draw_graph(mileage, prices, predicted_prices)


    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()