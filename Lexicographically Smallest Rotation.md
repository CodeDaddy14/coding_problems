## 01. Lexicographically Smallest Rotation

The problem can be found at the following link: [Question Link](https://www.geeksforgeeks.org/problems/lexicographically-smallest-string--151951/1?_gl=1*16p306d*_up*MQ..&gclid=CjwKCAjw25fWBhAVEiwAMopNjsmjyvUTHaI6nBTxpCneDBkO9vK1L2Q8vLcmcYfTVYf8-tXpMqdahhoCoXYQAvD_BwE&gbraid=0AAAAAC9yBkCxB9KL-tydjtd24SrU_lpRb)

### Problem Description

**Task:** Given a string s, find the lexicographically smallest string after rotating the string left any number of times including 0.Example:Input: s = "abcd"Output: "abcd"Explanation: String after each rotation are "abcd", "bcda", "cdab", "dabc" and so on. Lexicographically smallest among them is "abcd".Input: s = "baca"

#### Examples

##### Example 1

- **Output:**
```text
"abac"
```
- **Explanation:** Strings after each rotation are "baca", "acab", "caba", "abac" and so on. Lexicographically smallest among them is "abac".

### Time and Auxiliary Space Complexity

- **Expected Time Complexity:** O(n)
- **Expected Auxiliary Space Complexity:** O(n)

### Accepted Solutions (2)

#### Solution 1 (Python)

- **Submitted:** 2026-10-09 23:18:37
- **Status:** Correct
- **Marks:** 0

```python
class Solution:
    def lexiString(self, s: str) -> str:
        t = s+s
        i = 0
        j = 1
        k = 0
        n = len(s)

        while (i<n and j<n and k<n):
          if t[i+k] == t[j+k]:
            k+=1
            continue

          if t[i+k] > t[j+k]:
            i = i+k+1
          else:
            j=j+k+1

          if i==j:
            j+=1

          k=0

        start = min(i, j)
        return t[start:start + n]
        # return "".join(min([s[i:]+s[:i]] for i in range(len(s))))
```

#### Solution 2 (Python)

- **Submitted:** 2026-10-09 22:33:55
- **Status:** Correct
- **Marks:** 8

```python
class Solution:
    def lexiString(self, s: str) -> str:
        t = s+s
        i = 0
        j = 1
        k = 0
        n = len(s)

        while (i<n and j<n and k<n):
          if t[i+k] == t[j+k]:
            k+=1
            continue

          if t[i+k] > t[j+k]:
            i = i+k+1
          else:
            j=j+k+1

          if i==j:
            j+=1

          k=0

        start = min(i, j)
        return t[start:start + n]
        # return "".join(min([s[i:]+s[:i]] for i in range(len(s))))
```

*Generated on: 12/10/2026, 02:32:59*