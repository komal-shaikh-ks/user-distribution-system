class Worker:
    def __init__(self, worker_id, region):
        self.worker_id = worker_id
        self.region = region  # Worker coordinates (2D or 3D)
        self.assigned_users = []

    def add_user(self, user):
        self.assigned_users.append(user)

    def __repr__(self):
        return f"Worker {self.worker_id} at {self.region}"
