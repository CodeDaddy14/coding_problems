## 01. Perimeter of Shapes in Binary Matrix

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/find-perimeter-of-shapes/1?_gl=1*15cb36q*_up*MQ..&gclid=CjwKCAjw25fWBhAVEiwAMopNjsmjyvUTHaI6nBTxpCneDBkO9vK1L2Q8vLcmcYfTVYf8-tXpMqdahhoCoXYQAvD_BwE&gbraid=0AAAAAC9yBkCxB9KL-tydjtd24SrU_lpRb)

### Problem Description

**Task:** Given a binary matrix mat[][] of size n × m, where each cell contains either 0 or 1, find the total perimeter of all figures formed by cells containing 1s. Two cells are considered adjacent if they share a common side.
A single cell containing 1 has a perimeter of 4, whereas two adjacent cells containing 1 (i.e., 11) together have a perimeter of 6.

#### Examples

##### Example 1

- **Input:**
```text
mat[][] = [[0,1,0,0,0], [1,1,1,0,0], [1,0,0,0,0]]Output: 12Explanation: The five cells form a single figure. Hence, the perimeter of the figure is 12.
```

##### Example 2

- **Input:**
```text
mat[][] = [[1,0], [1,1]]Output: 8Explanation: The two adjacent cells share one common side. Hence, the perimeter of the figure is 6.
```

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n * m)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-10-05 17:03:25
- **Status:** Correct
- **Marks:** 2

```python
class Solution:
    def findPerimeter(self, mat):
        perimeter = 0

        for i in range(len(mat)):
            for j in range(len(mat[0])):

                if mat[i][j] == 1:
                    perimeter += 4

                    if i > 0 and mat[i - 1][j] == 1:
                        perimeter -= 2

                    if j > 0 and mat[i][j - 1] == 1:
                        perimeter -= 2

        return perimeter
```

*Generated on: 12/10/2026, 02:34:49*