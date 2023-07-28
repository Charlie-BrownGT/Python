import math

def calculate_circle_area(radius):
    return math.pi * radius**2

def main():
    try:
        radius = float(input("Enter the radius of the circle: "))
        if radius <= 0:
            print("Please enter a positive value for the radius.")
        else:
            area = calculate_circle_area(radius)
            print(f"The area of the circle with radius {radius} is: {area:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid number for the radius.")

if __name__ == "__main__":
    main()


python circle_area.py
