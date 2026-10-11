## 01. Your Social Network

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/your-social-network0328/1?_gl=1*6mfvsj*_up*MQ..&gclid=CjwKCAjw25fWBhAVEiwAMopNjsmjyvUTHaI6nBTxpCneDBkO9vK1L2Q8vLcmcYfTVYf8-tXpMqdahhoCoXYQAvD_BwE&gbraid=0AAAAAC9yBkCxB9KL-tydjtd24SrU_lpRb)

### Problem Description

**Task:** Geek is creating a social networking site called Geeksbook with n users numbered from 1 to n. Each user i (2 ≤ i ≤ n) has exactly one friend, and that friend must have a smaller user number than i. User 1 has no friend. The friends of users 2 to n are given in an array arr[] of size n - 1, where:
arr[0] is the friend of user 2.
arr[1] is the friend of user 3.
...
arr[i - 2] is the friend of user i.
The relationship is one-way. A user can reach another user by repeatedly following their friend's link. For every user i from 2 to n, find all users j (1 ≤ j < i) that can be reached from i. For every reachable pair (i, j), create an array [i, j, k] where:
i is the starting user.
j is the reachable user.
k is the number of links that must be followed to reach j from i.
The result should contain these arrays in the following order:
Process users i from 2 to n.
For each user i, consider users j from 1 to i - 1 in increasing order.
Include [i, j, k] only if j is reachable from i.
Return a 2D array containing information about all reachable pairs.

#### Examples

##### Example 1

- **Input:**
```text
arr[] = [1, 2]
```
- **Output:**
```text
[[2, 1, 1], [3, 1, 2], [3, 2, 1]]
```
- **Explanation:** The links are 2 → 1 and 3 → 2. User 2 can reach user 1 in 1 link. User 3 can reach user 1 in 2 links. User 3 can reach user 2 in 1 link.

##### Example 2

- **Input:**
```text
arr[] = [1, 1]
```
- **Output:**
```text
[[2, 1, 1], [3, 1, 1]]
```
- **Explanation:** The links are 2 → 1 and 3 → 1. User 2 can reach user 1 in 1 link. User 3 can reach user 1 in 1 link.

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n^2)
- **Expected Auxiliary Space Complexity:** O(n^2)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-10-12 01:58:44
- **Status:** Correct
- **Marks:** 4

```python
class Solution:
    def socialNetwork(self, arr):
        friend = arr
        ans = []
        for user in range(2,len(friend)+2):
          current_user = user
          step = 0
          current_group = []
          while current_user != 1:
            current_user = friend[current_user - 2]
            step+=1
            current_group.append([user,current_user,step])
          ans.extend(current_group[::-1])
        return ans
```

*Generated on: 12/10/2026, 02:30:47*