#Coordinate Frame
import math

x = float(input("Robot x position: "))
y = float(input("Robot y position: "))
theta = float(input("Robot orientation (rad): "))

xr = float(input("Point x in robot frame: "))
yr = float(input("Point y in robot frame: "))

xw = x + xr * math.cos(theta) - yr * math.sin(theta)
yw = y + xr * math.sin(theta) + yr * math.cos(theta)

print(f"World Frame Point: x={xw:.2f}, y={yw:.2f}")
