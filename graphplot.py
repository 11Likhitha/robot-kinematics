#graphplot
import math
import matplotlib.pyplot as plt

# Initial state
x, y, theta = 0.0, 0.0, 0.0

v = 0.5
omega = 0.2
dt = 0.1

# Store trajectory
x_points = []
y_points = []

for step in range(50):   # increase steps to see curve clearly
    x += v * math.cos(theta) * dt
    y += v * math.sin(theta) * dt
    theta += omega * dt

    x_points.append(x)
    y_points.append(y)

# Plot
plt.figure()
plt.plot(x_points, y_points, marker='o')
plt.xlabel("X position (m)")
plt.ylabel("Y position (m)")
plt.title("Robot Trajectory")
plt.grid()

plt.axis("equal")  # important for correct shape
plt.show()
