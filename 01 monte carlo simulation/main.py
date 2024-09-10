import numpy as np
import matplotlib.pyplot as plt

# Set the radius of the quarter circle
radius = int(input("Enter the Radius"))

# Number of random points to generate
N = int(input("Enter the No. of random points to generate"))

# Generate N random x-coordinates between 0 and the radius
x_random = np.random.uniform(0, radius, N)

# Generate N random y-coordinates between 0 and the radius
y_random = np.random.uniform(0, radius, N)

# Check if each point (x, y) lies inside the quarter circle.
# A point is inside if x^2 + y^2 <= r^2 (equation of a circle with radius r).
inside_circle = (x_random**2 + y_random**2) <= radius**2

# Count the number of points that are inside the quarter circle
n = np.sum(inside_circle)

# Estimate the area of the quarter circle:
# The ratio of points inside the quarter circle (n / N) multiplied by the area of the square (r^2).
area_quarter_circle = (n / N) * (radius * radius)

# Estimate the value of π from the area of the quarter circle:
# Since the area of a full circle is π * r^2 and the area of the quarter circle is (π * r^2) / 4,
# we multiply the area of the quarter circle by 4 and divide by r^2 to estimate π.
pi_estimate = (area_quarter_circle * 4) / (radius * radius)

# Display the results
print(f"Estimated π = {pi_estimate}")
print(f"Analytical π = {np.pi}")
print(f"Error = {abs(np.pi - pi_estimate)}")
print(f"Error % = {abs(np.pi - pi_estimate) / np.pi * 100:.2f}%")

# Prepare to plot the actual quarter circle for reference.
theta = np.linspace(0, np.pi / 2, 1000)  # Generate angles from 0 to π/2 (for quarter circle)
x_circle = radius * np.cos(theta)  # x-coordinates of the quarter circle
y_circle = radius * np.sin(theta)  # y-coordinates of the quarter circle

# Create a plot to visualize the points and the quarter circle.
plt.figure(figsize=(6, 6))  # Set the figure size to be square
plt.plot(x_circle, y_circle, color='blue', label='Quarter circle')  # Plot the quarter circle
plt.scatter(x_random[inside_circle], y_random[inside_circle], color='green', s=1, label='Points inside circle')  # Plot points inside the quarter circle
plt.scatter(x_random[~inside_circle], y_random[~inside_circle], color='red', s=1, label='Points outside circle')  # Plot points outside the quarter circle
plt.xlim(0, radius)  # Set the x-axis limit to the radius
plt.ylim(0, radius)  # Set the y-axis limit to the radius
plt.gca().set_aspect('equal', adjustable='box')  # Ensure equal aspect ratio for x and y axes
plt.xlabel('x')  # Label for x-axis
plt.ylabel('y')  # Label for y-axis
plt.title('Monte Carlo Method to Estimate π')  # Title of the plot
plt.legend()  # Display the legend
plt.grid(True)  # Enable grid for better visualization
plt.show()  # Show the plot
