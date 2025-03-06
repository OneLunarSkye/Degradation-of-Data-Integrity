import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation

# Define the system of differential equations
def system(x, t):
    x1, x2 = x
    dx1dt = 0.1 * x2 - 0.05 * x1  # Adjusted coefficients for slower evolution
    dx2dt = -0.1 * x2 + 0.05 * x1  # Adjusted coefficients
    return [dx1dt, dx2dt]

# Initial conditions (starting values of x1 and x2)
x0 = [1, 1]  # x1(0) = 1, x2(0) = 1

# Time vector from t=0 to t=100 (extended duration for gradual change)
t = np.linspace(0, 100, 500)

# Solve the differential equations
sol = odeint(system, x0, t)

# Plot the solutions
plt.figure(figsize=(10, 6))
plt.plot(t, sol[:, 0], label="x1(t) - Processor A", color="blue")
plt.plot(t, sol[:, 1], label="x2(t) - Processor B", color="red")
plt.title("Data in Processors A and B over Time")
plt.xlabel("Time (t)")
plt.ylabel("Data (MB)")
plt.legend()
plt.grid(True)
plt.show()

# For animation (adjust to slower, clearer pace)
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 100)  # Time range
ax.set_ylim(min(np.min(sol), 0) - 1, np.max(sol) + 1)  # Dynamic y-range

# Plot the lines for x1 and x2
line_x1, = ax.plot([], [], label="x1(t) - Processor A", color="blue")
line_x2, = ax.plot([], [], label="x2(t) - Processor B", color="red")

# Set titles and labels for the animation
ax.set_title("Animation of Data in Processors A and B")
ax.set_xlabel("Time (t)")
ax.set_ylabel("Data (MB)")
ax.legend()

# Initialize the plot
def init():
    line_x1.set_data([], [])
    line_x2.set_data([], [])
    return line_x1, line_x2

# Update the plot for animation frames
def update(frame):
    line_x1.set_data(t[:frame], sol[:frame, 0])  # Update x1
    line_x2.set_data(t[:frame], sol[:frame, 1])  # Update x2
    return line_x1, line_x2

# Create the animation
ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True)

# Show the animation
plt.show()
