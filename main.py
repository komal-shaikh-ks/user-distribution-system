from distribution import UserDistribution

def main():
    # Parameters: number of users, number of workers, dimensions (2D or 3D)
    num_users = 10000
    num_workers = 100
    dimensions = 3  # 2D or 3D space

    # Initialize and distribute users across workers
    user_dist = UserDistribution(num_users, num_workers, dimensions)
    
    # Visualize the results
    user_dist.visualize()

if __name__ == "__main__":
    main()
