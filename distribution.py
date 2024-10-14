import numpy as np
from scipy.spatial import Voronoi
from worker import Worker
from user import User
from visualization import Visualizer

class UserDistribution:
    def __init__(self, num_users, num_workers, dimensions):
        self.num_users = num_users
        self.num_workers = num_workers
        self.dimensions = dimensions

        # Initialize users and workers with random positions in space
        self.users = [User(i, np.random.rand(self.dimensions)) for i in range(self.num_users)]
        self.workers = [Worker(i, np.random.rand(self.dimensions)) for i in range(self.num_workers)]
        
        # Distribute users across workers
        self.distribute_users()

    def distribute_users(self):
        # Voronoi partitioning for worker regions
        worker_positions = np.array([worker.region for worker in self.workers])
        vor = Voronoi(worker_positions)
        
        # Assign each user to the closest worker using Voronoi regions
        for user in self.users:
            distances = np.linalg.norm(worker_positions - user.location, axis=1)
            nearest_worker = np.argmin(distances)
            self.workers[nearest_worker].add_user(user)
        
        # Balance load to ensure each worker has an approximately equal number of users
        self.balance_load()

    def balance_load(self):
        avg_users_per_worker = self.num_users // self.num_workers
        excess_users = []

        for worker in self.workers:
            while len(worker.assigned_users) > avg_users_per_worker:
                excess_users.append(worker.assigned_users.pop())
        
        # Reassign excess users to workers with fewer users
        for worker in self.workers:
            while len(worker.assigned_users) < avg_users_per_worker and excess_users:
                worker.add_user(excess_users.pop())

    def visualize(self):
        # 2D or 3D visualization
        visualizer = Visualizer(self.users, self.workers, self.dimensions)
        visualizer.display()
