def min_tries_for_x(num_floors, num_balls):
    memo = [[0] * (num_balls + 1) for _ in range(num_floors + 1)]

    for i in range(1, num_balls + 1):
        memo[1][i] = 1

    for i in range(1, num_floors + 1):
        memo[i][1] = i

    for i in range(2, num_floors + 1):
        for j in range(2, num_balls + 1):
            memo[i][j] = float("inf")
            for x in range(1, i + 1):
                worst_case = 1 + max(memo[x - 1][j - 1], memo[i - x][j])
                memo[i][j] = min(memo[i][j], worst_case)

    return memo[num_floors][num_balls]

def main():
    print("Enter the number of floors:")
    num_floors = int(input())

    print("Enter the number of balls:")
    num_balls = int(input())

    min_tries = min_tries_for_x(num_floors, num_balls)
    print(f"Minimum number of throws needed to find X: {min_tries}")

if __name__ == "__main__":
    main()
