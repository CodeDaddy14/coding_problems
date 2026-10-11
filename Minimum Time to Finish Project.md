## 01. Minimum Time to Finish Project

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/project-manager--141631/1?_gl=1*vv30di*_up*MQ..&gclid=CjwKCAjw25fWBhAVEiwAMopNjsmjyvUTHaI6nBTxpCneDBkO9vK1L2Q8vLcmcYfTVYf8-tXpMqdahhoCoXYQAvD_BwE&gbraid=0AAAAAC9yBkCxB9KL-tydjtd24SrU_lpRb)

### Problem Description

**Task:** An IT company is working on a large project consisting of n modules. The given array time required (in months) to complete the i^th module is stored in the array duration[]. The array dependencies[][], where dependencies[i] = [u, v], indicates that module v can be started only after module u is completed. Multiple modules can be worked on simultaneously as long as all their dependencies have been completed. Find the minimum time required to complete the entire project. If the project cannot be completed due to a cyclic dependency, return -1. A module is never dependent on itself.ExamplesInput: duration[] = [10, 20, 30, 10, 30, 20], dependencies[][] = [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]

#### Examples

##### Example 1

- **Output:**
```text
-1
```
- **Explanation:** There is a cycle in the dependency graph hence the project cannot be completed.

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n + m)
- **Expected Auxiliary Space Complexity:** O(n)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-10-08 14:48:18
- **Status:** Correct
- **Marks:** 4

```python
class Solution:
    def minTime(self, duration, dependencies):
        from collections import deque
        n = len(duration)
        adj = [[] for _ in range(n)]
        indeg = [0]*n
        time = [0]*n
        processed = 0

        for u,v in dependencies:
          adj[u].append(v)
          indeg[v]+=1

        q = deque()
        for i in range(n):
            if indeg[i] == 0:
                time[i] = duration[i]
                q.append(i)

        while q:
          u = q.popleft()
          processed+=1
          for v in adj[u]:
            time[v] = max(time[v],time[u]+duration[v])
            indeg[v]-=1
            if indeg[v] == 0:
              q.append(v)
        
        return (max(time) if processed == n else -1)
```

*Generated on: 12/10/2026, 02:31:48*