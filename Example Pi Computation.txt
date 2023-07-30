import random

def calculate_pi(num_points):
    inside_circle = 0

    for _ in range(num_points):
        x = random.random()
        y = random.random()

        distance_squared = x**2 + y**2
        if distance_squared <= 1:
            inside_circle += 1

    pi_estimate = 4 * inside_circle / num_points
    return pi_estimate

def main():
    try:
        num_points = int(input("Enter the number of points to use in the calculation: "))
        if num_points <= 0:
            print("Please enter a positive value for the number of points.")
        else:
            pi_approximation = calculate_pi(num_points)
            print(f"Approximated value of pi using {num_points} points: {pi_approximation:.6f}")
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of points.")

if __name__ == "__main__":
    main()
