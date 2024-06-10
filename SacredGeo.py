import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to create the Flower of Life in 2D
def flower_of_life_2d(radius=1, num_circles=7):
    angles = np.linspace(0, 2 * np.pi, 100)
    circles = []
    for i in range(num_circles):
        for j in range(num_circles):
            x_offset = radius * (i - num_circles//2) * 1.5
            y_offset = radius * (j - num_circles//2) * np.sqrt(3)
            if (i + j) % 2 == 0:
                x = x_offset + radius * np.cos(angles)
                y = y_offset + radius * np.sin(angles)
                circles.append((x, y))
    return circles

# Plot the 2D Flower of Life
circles = flower_of_life_2d()
plt.figure(figsize=(8, 8))
for circle in circles:
    plt.plot(circle[0], circle[1], 'b')
plt.axis('equal')
plt.title('2D Flower of Life')
plt.show()

# Extend to 3D by adding layers of circles
def flower_of_life_3d(radius=1, num_layers=3):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for layer in range(num_layers):
        z_offset = layer * (radius * np.sqrt(2) / 2)
        circles = flower_of_life_2d(radius=radius, num_circles=7)
        for circle in circles:
            ax.plot(circle[0], circle[1], zs=z_offset, zdir='z', color='b')
    ax.set_title('3D Flower of Life')
    plt.show()

# Plot the 3D Flower of Life
flower_of_life_3d()


from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define vertices for Metatron's Cube
vertices = np.array([[1, 1, 1], [1, 1, -1], [1, -1, -1], [1, -1, 1],
                     [-1, 1, 1], [-1, 1, -1], [-1, -1, -1], [-1, -1, 1]])

# Define edges connecting the vertices
edges = [[vertices[j] for j in [0, 1, 2, 3]],
         [vertices[j] for j in [4, 5, 6, 7]],
         [vertices[j] for j in [0, 3, 7, 4]],
         [vertices[j] for j in [1, 2, 6, 5]],
         [vertices[j] for j in [0, 1, 5, 4]],
         [vertices[j] for j in [2, 3, 7, 6]]]

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the edges
for edge in edges:
    ax.add_collection3d(Poly3DCollection([edge], facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

# Set plot limits
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])
ax.set_title('Metatron\'s Cube')
plt.show()

# Define the grid
x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)

# Define wave sources based on Flower of Life pattern
def wave_source(X, Y, x0, y0):
    return np.sin(np.sqrt((X - x0)**2 + (Y - y0)**2))

# Sum of multiple wave sources
Z = wave_source(X, Y, 0, 0)
for i in range(1, 7):
    Z += wave_source(X, Y, np.cos(i * np.pi / 3), np.sin(i * np.pi / 3))

plt.contourf(X, Y, Z, cmap='viridis')
plt.title("Wave Interference Pattern with Flower of Life")
plt.show()

from scipy.integrate import odeint

# Define a system of differential equations
def model(y, t):
    dydt = [y[1], -0.5*y[1] - y[0] + np.cos(t)]
    return dydt

# Initial conditions
y0 = [0.5, 0]

# Time points
t = np.linspace(0, 20, 400)

# Solve ODE
sol = odeint(model, y0, t)

# Plot results
plt.plot(t, sol[:, 0], label='y(t)')
plt.plot(t, sol[:, 1], label='dy/dt(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.title("Differential Equation Solutions")
plt.show()
