import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameters of the mass-spring-damper system
m = 250.0   # Mass (kg)
c = 250.0   # Damping coefficient (Ns/m)
k = 8000.0  # Spring constant (N/m)

# Define the external force as a function of time (sinusoidal force)
def f(t):
    return np.sin(2 * np.pi * t)  # Sinusoidal force with a frequency of 1 Hz

# Define the system of differential equations for the mass-spring-damper system
def system(x, t):
    x1, x1_dot = x  # x1 is displacement, x1_dot is velocity
    # Second-order ODE split into two first-order equations
    x1_ddot = (f(t) - c * x1_dot - k * x1) / m  # Acceleration (second derivative of displacement)
    return [x1_dot, x1_ddot]  # Return velocity and acceleration

# Initial conditions: displacement = 0, velocity = 0
x0 = [0.0, 0.0]

# Time vector (from 0 to 5 seconds, 500 points)
t = np.linspace(0, 5, 500)

# Solve the system of differential equations using odeint
# 'solution' contains the time evolution of displacement and velocity
solution = odeint(system, x0, t)

# Extract the displacement (first column of the solution array)
x = solution[:, 0]

# Plotting the results
plt.plot(t, x, label='Displacement (X)')  # Plot the displacement over time
plt.plot(t, f(t), label='External Force (f(t))', linestyle='dashed')  # Plot the external force as a reference
plt.xlabel('Time [s]')  # X-axis label (time in seconds)
plt.ylabel('Displacement [m]')  # Y-axis label (displacement in meters)
plt.title('Mass-Spring-Damper System')  # Title of the plot
plt.legend()  # Display the legend (label of each plot)
plt.grid(True)  # Add a grid to the plot for better visualization
plt.show()  # Display the plot
