import json


def get_thetas_from_file(file):
    with open(file, "r") as file:
        thetas = json.load(file)
    theta0 = float(thetas["theta0"])
    theta1 = float(thetas["theta1"])
    return theta0, theta1


def main():
    parameters_file = "thetas.json"

    theta0 = 0.0
    theta1 = 0.0

    try:
        # Load the parameters saved from the training program
        theta0, theta1 = get_thetas_from_file(parameters_file)
    except ValueError:
        print("Warning: Thetas must be float. Tethas set to 0.")
    except Exception as e:
        pass
        
    try:
        # Prompt the user for mileage
        mileage = float(input("Enter the mileage(km): "))

        # Predict the price based on the loaded parameters
        predicted_price = theta0 + theta1 * mileage

        # Display the result
        print(f"The estimated price for a car with {mileage} km is: {predicted_price:.2f}")

    except ValueError:
        print("Invalid input. Please enter a numeric value for mileage.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
