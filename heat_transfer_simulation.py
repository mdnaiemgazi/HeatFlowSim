# --------------------------- Heat Transfer Simulation --------------------------- #
# Title: Simulation of Heat Transfer in Mechanical Systems using Finite Difference Method
# Description: A Python simulation to model 1D heat conduction through a metal rod
#              using numerical methods and visualize temperature distribution over time.
# Author: MD Naiem Gazi
# ------------------------------------------------------------------------------- #

# Step 1: Import necessary libraries for numerical computation and plotting
# ------------------------------------------------------------------------------
import numpy as np  # For numerical operations
import matplotlib.pyplot as plt  # For plotting results

# Step 2: Define the simulation parameters and constants
# ------------------------------------------------------------------------------
length = 1.0  # Length of the rod (in meters)
nx = 20  # Number of spatial points (discretizing the rod)
dx = length / (nx - 1)  # Spatial step size (distance between points)
alpha = 1e-4  # Thermal diffusivity of the material (in m^2/s)

# Define time parameters
total_time = 10.0  # Total simulation time (in seconds)
dt = 0.01  # Time step for simulation (in seconds)
nt = int(total_time / dt)  # Number of time steps

# Define initial and boundary conditions
T_left = 100.0  # Left boundary temperature (fixed at 100°C)
T_right = 50.0  # Right boundary temperature (fixed at 50°C)
T_initial = 25.0  # Initial temperature of the entire rod (25°C)

# Step 3: Initialize the temperature distribution array
# ------------------------------------------------------------------------------
# Create a numpy array to store temperature values at each spatial point
T = np.ones(nx) * T_initial  # Initially, all points are at the initial temperature (25°C)
T[0] = T_left  # Apply left boundary condition
T[-1] = T_right  # Apply right boundary condition

# Step 4: Define the finite difference update rule for heat conduction
# ------------------------------------------------------------------------------
def update_temperature(T, alpha, dx, dt):
    """
    This function computes the next time step for the temperature array
    using the explicit finite difference method.
    """
    T_new = T.copy()  # Create a copy of the temperature array to store updated values
    for i in range(1, nx - 1):
        # Apply the finite difference formula for each interior point
        T_new[i] = T[i] + alpha * dt / dx**2 * (T[i + 1] - 2 * T[i] + T[i - 1])
    return T_new

# Step 5: Time loop for simulation over the defined time period
# ------------------------------------------------------------------------------
# Create an array to store the temperature history at each time step
T_history = []

# Main time-stepping loop
for n in range(nt):
    # Update the temperature for the next time step
    T = update_temperature(T, alpha, dx, dt)
    T_history.append(T.copy())  # Store the updated temperature array at each time step

# Convert the T_history list to a numpy array for easier manipulation and plotting
T_history = np.array(T_history)

# Step 6: Plot the results to visualize the temperature distribution
# ------------------------------------------------------------------------------
# Create spatial points for the x-axis (rod length)
x = np.linspace(0, length, nx)

# Choose a few time points to plot the temperature distribution
time_points = [0, nt // 4, nt // 2, nt - 1]  # Start, 1/4th, half, and end of simulation

# Set up the plot
plt.figure(figsize=(10, 6))

# Plot the temperature distribution at selected time points
for time_point in time_points:
    plt.plot(x, T_history[time_point], label=f'Time = {time_point * dt:.2f}s')

# Add labels, title, and legend to the plot
plt.xlabel('Position along the rod (m)')
plt.ylabel('Temperature (°C)')
plt.title('1D Heat Conduction in a Metal Rod')
plt.legend()
plt.grid(True)  # Add gridlines to the plot

# Show the plot with temperature distribution
plt.show()
