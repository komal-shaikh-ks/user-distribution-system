import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Visualizer:
    def __init__(self, users, workers, dimensions):
        self.users = users
        self.workers = workers
        self.dimensions = dimensions

    def display(self):
        if self.dimensions == 2:
            self._plot_2d()
        elif self.dimensions == 3:
            self._plot_3d()

    def _plot_2d(self):
        plt.figure(figsize=(8, 8))

        # Plot workers in red
        for worker in self.workers:
            plt.scatter(worker.region[0], worker.region[1], c='red', s=100)

        # Plot users in blue
        for user in self.users:
            plt.scatter(user.location[0], user.location[1], c='blue', s=10)

        plt.title("2D User-Worker Distribution")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()

    def _plot_3d(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        # Plot workers in red
        for worker in self.workers:
            ax.scatter(worker.region[0], worker.region[1], worker.region[2], c='red', s=100)

        # Plot users in blue
        for user in self.users:
            ax.scatter(user.location[0], user.location[1], user.location[2], c='blue', s=10)

        ax.set_title("3D User-Worker Distribution")
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        plt.show()
