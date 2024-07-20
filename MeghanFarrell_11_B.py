import math

def calculate_hypotenuse():
    # Prompt user to input the nearest angle in degrees
    nearest_angle = float(input("Enter the nearest angle in degrees: "))

    # Prompt user to input the length of the adjacent side
    adjacent_side = float(input("Enter the length of the adjacent side: "))

    # Convert nearest angle from degrees to radians
    angle_radians = math.radians(nearest_angle)

    # Calculate the hypotenuse using the cosine function
    hypotenuse = adjacent_side / math.cos(angle_radians)

    # Print the length of the hypotenuse
    print(f"The length of the hypotenuse is: {hypotenuse:.2f}")

# Execute the function
calculate_hypotenuse()