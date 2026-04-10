#Forward Kinematics
import math

x, y, theta = 0.0, 0.0, 0.0
v = 0.5
omega = 0.2
dt = 0.1

for step in range(5):
    x += v * math.cos(theta) * dt
    y += v * math.sin(theta) * dt
    theta += omega * dt
    print(f"Step {step+1}: x={x:.2f}, y={y:.2f}, theta={theta:.2f}")
