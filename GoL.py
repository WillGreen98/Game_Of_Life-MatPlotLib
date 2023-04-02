import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider


N = 50
generations = 50

grid = np.random.choice([0, 1], size=(N, N), p=[0.7, 0.3])


def update_grid(frame_number):
    global grid, N, mat
    new_grid = np.copy(grid)
    for i in range(N):
        for j in range(N):
            neighbors = (grid[(i-1)%N,(j-1)%N] + grid[(i-1)%N,j] + grid[(i-1)%N,(j+1)%N] +
                         grid[i,(j-1)%N] + grid[i,(j+1)%N] +
                         grid[(i+1)%N,(j-1)%N] + grid[(i+1)%N,j] + grid[(i+1)%N,(j+1)%N])
            if grid[i,j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i,j] = 0
            elif grid[i,j] == 0 and neighbors == 3:
                new_grid[i,j] = 1
    grid[:] = new_grid[:]
    mat.set_data(grid)

    return mat,


fig, ax = plt.subplots()
mat = ax.matshow(grid, cmap=plt.cm.Greens)

ax_N = plt.axes([0.25, 0.02, 0.65, 0.03])
ax_generations = plt.axes([0.25, 0.05, 0.65, 0.03])
slider_N = Slider(ax=ax_N, label='N', valmin=10, valmax=100, valinit=N, valstep=1)
slider_generations = Slider(ax=ax_generations, label='Generations', valmin=10, valmax=100, valinit=generations, valstep=1)


def update(val):
    global N, generations, grid, ani
    N = int(slider_N.val)
    generations = int(slider_generations.val)
    grid = np.random.choice([0, 1], size=(N, N), p=[0.7, 0.3])
    ani.event_source.stop()
    ani = animation.FuncAnimation(fig, update_grid, frames=generations, interval=100, save_count=50)
    plt.show()


slider_N.on_changed(update)
slider_generations.on_changed(update)

ani = animation.FuncAnimation(fig, update_grid, frames=generations, interval=100, save_count=50)

plt.show()