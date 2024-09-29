import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def num_paths(m, n, heights, i, j, memo):
  # If we've reached the destination point, return 1
  if i == m - 1 and j == n - 1:
    return 1

  # If the result for this point has already been calculated, return it
  if memo[i][j] != -1:
    return memo[i][j]

  # Initialize the number of paths to 0
  paths = 0

  # Try moving to the points to the top, bottom, left, and right
  if i > 0 and heights[i-1][j] < heights[i][j]:
    paths += num_paths(m, n, heights, i-1, j, memo)
  if i < m - 1 and heights[i+1][j] < heights[i][j]:
    paths += num_paths(m, n, heights, i+1, j, memo)
  if j > 0 and heights[i][j-1] < heights[i][j]:
    paths += num_paths(m, n, heights, i, j-1, memo)
  if j < n - 1 and heights[i][j+1] < heights[i][j]:
    paths += num_paths(m, n, heights, i, j+1, memo)

  # Store the result in the memoization table
  memo[i][j] = paths

  # Return the total number of paths
  return paths

# Read the input
m, n = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(m)]

# Initialize the memoization table with -1
memo = [[-1 for _ in range(n)] for _ in range(m)]

# Print the result
print(num_paths(m, n, heights, 0, 0, memo))
