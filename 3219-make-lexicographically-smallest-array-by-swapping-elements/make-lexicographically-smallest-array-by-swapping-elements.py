class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        pairs = [(nums[i], i) for i in range(len(nums))]
        pairs.sort()
        
        group_boundaries = [0]
        for k in range(1, len(pairs)):
            if abs(pairs[k][0] - pairs[k-1][0]) > limit:
                group_boundaries.append(k)
        group_boundaries.append(len(pairs))
        
        result = [0] * len(nums)
        for g in range(len(group_boundaries) - 1):
            start, end = group_boundaries[g], group_boundaries[g+1]
            group = pairs[start:end]
            values = sorted(v for v, i in group)
            indices = sorted(i for v, i in group)
            for idx, val in zip(indices, values):
                result[idx] = val
        
        return result