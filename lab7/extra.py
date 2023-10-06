import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


def update(frame):
    line.set_ydata(np.sin(x_values + frame / 10))
    return line,


x_values = np.linspace(0, 2 * np.pi, 100)
y_values = np.sin(x_values)

fig, ax = plt.subplots()

line, = ax.plot(x_values, y_values, label='y = sin(x)')

ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Анимация функции y = sin(x)')

animation = FuncAnimation(fig, update, frames=range(100), blit=True)

animation_file = 'sin_animation.gif'
animation.save(animation_file, writer=PillowWriter(fps=10))

plt.show()
