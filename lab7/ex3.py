import numpy as np
import matplotlib.pyplot as plt

x_values = np.linspace(-np.pi, np.pi, 100)
y_values = x_values
z_values = np.tan(x_values)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

ax.plot(x_values, y_values, z_values, label='z=tg(x)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Трёхмерный график для x∈(-п;п); y=x; z=tg(x)')

plt.show()
