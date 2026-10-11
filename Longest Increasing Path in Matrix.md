## 01. Longest Increasing Path in Matrix

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/longest-increasing-path-in-a-matrix/1?_gl=1*butaw7*_up*MQ..&gclid=CjwKCAjw25fWBhAVEiwAMopNjsmjyvUTHaI6nBTxpCneDBkO9vK1L2Q8vLcmcYfTVYf8-tXpMqdahhoCoXYQAvD_BwE&gbraid=0AAAAAC9yBkCxB9KL-tydjtd24SrU_lpRb)

### Problem Description

**Task:** Given a matrix with n rows and m columns, find the length of the longest path such that:The path can start and end at any cell.A cell cannot be visited more than once.The values in path are strictly increasing. From each cell, you can move left, right, up, or down. Diagonal moves and moves outside the matrix are not allowed.Examples:Input: n = 3, m = 3, matrix[][] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#### Examples

##### Example 1

- **Output:**
```text
1
```
- **Explanation:** There can at most one vertex as all vertices are same.

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n * m)
- **Expected Auxiliary Space Complexity:** O(n * m)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-10-12 02:53:55
- **Status:** Correct
- **Marks:** 8

```python
class Solution:
    def longIncPath(self, matrix, n, m):
        dp = [[0] * m for _ in range(n)]   # dp[i][j] = longest path starting at (i, j)

        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]
            best = 1
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and matrix[ni][nj] > matrix[i][j]:
                    best = max(best, 1 + dfs(ni, nj))
            dp[i][j] = best
            return best

        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans, dfs(i, j))
        return ans
```

*Generated on: 12/10/2026, 02:54:25*