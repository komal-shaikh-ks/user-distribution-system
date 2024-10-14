class User:
    def __init__(self, user_id, location):
        self.user_id = user_id
        self.location = location  # User's position in space (2D or 3D)

    def __repr__(self):
        return f"User {self.user_id} at {self.location}"
