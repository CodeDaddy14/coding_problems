## 01. Maximum Frequency with K Increments

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/maximum-frequency-1662528911/1?_gl=1*1ve53cf*_up*MQ..&gclid=CjwKCAjw25fWBhAVEiwAMopNjsmjyvUTHaI6nBTxpCneDBkO9vK1L2Q8vLcmcYfTVYf8-tXpMqdahhoCoXYQAvD_BwE&gbraid=0AAAAAC9yBkCxB9KL-tydjtd24SrU_lpRb)

### Problem Description

**Task:** Given an integer array arr[]. In one operation, you can choose an index and increment its value by 1.Find the maximum possible frequency of any element after performing at most k operations.Examples:Input: arr[] = [2, 2, 4], k = 4

#### Examples

##### Example 1

- **Output:**
```text
3
```
- **Explanation:** Apply two increment operations on index 0 and two operations on index 1 to make arr[] = [4, 4, 4]. Frequency of 4 is 3.

##### Example 2

- **Input:**
```text
arr[] = [7, 7, 7, 7], k = 5
```
- **Output:**
```text
4
```
- **Explanation:** The frequency of 7 is already 4, so no operations are needed.

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n log n)
- **Expected Auxiliary Space Complexity:** O(1)

### Accepted Solutions (1)

#### Solution 1 (Python)

- **Submitted:** 2026-10-12 14:10:12
- **Status:** Correct
- **Marks:** 4

```python
class Solution:
    def maxFrequency(self, arr, k):
        arr.sort()
        l = 0
        window_sum = 0
        best = 0

        for r in range(len(arr)):
            window_sum += arr[r]
            # cost to raise the whole window to arr[r]
            while arr[r] * (r - l + 1) - window_sum > k:
                window_sum -= arr[l]
                l += 1
            best = max(best, r - l + 1)

        return best
```

*Generated on: 12/10/2026, 14:10:47*