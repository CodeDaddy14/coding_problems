## 01. Coils in Matrix

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/form-coils-in-a-matrix4726/1?_gl=1*ws27q3*_up*MQ..&gclid=CjwKCAjw25fWBhAVEiwAMopNjsmjyvUTHaI6nBTxpCneDBkO9vK1L2Q8vLcmcYfTVYf8-tXpMqdahhoCoXYQAvD_BwE&gbraid=0AAAAAC9yBkCxB9KL-tydjtd24SrU_lpRb)

### Problem Description

**Task:** Given a positive integer n, consider a 4n * 4n matrix filled with integers from 1 to (4n) * (4n) in row-major order (left to right, top to bottom). Form two coils from the matrix:The first coil starts from the top-left cell (0, 0) and spirals inward.The second coil starts from the bottom-right cell (4n - 1, 4n - 1) and spirals inward in the opposite direction.Return these two coils in the same order.Examples:Input: n = 1Output: [[1, 5, 9, 13, 14, 15, 11, 7], [16, 12, 8, 4, 3, 2, 6, 10]]

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n^2)
- **Expected Auxiliary Space Complexity:** O(n^2)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-10-09 23:21:10
- **Status:** Correct
- **Marks:** 4

```python
class Solution:
    def formCoils(self, n: int) -> list[list[int]]:
        m = 8 * n * n                       # cells in each coil
        cur = 8 * n * n + 2 * n             # first cell of coil 1
        c1 = [cur]
        sign, step = 1, 2                   # sign=+1: up, right | sign=-1: down, left

        while len(c1) < m:
            for _ in range(step):           # vertical part
                cur -= sign * 4 * n
                c1.append(cur)
                if len(c1) == m: break
            if len(c1) == m: break
            for _ in range(step):           # horizontal part
                cur += sign
                c1.append(cur)
                if len(c1) == m: break
            sign = -sign
            step += 2

        c2 = [16 * n * n + 1 - x for x in c1]
        return [c2[::-1], c1[::-1]]
```

*Generated on: 12/10/2026, 02:33:48*