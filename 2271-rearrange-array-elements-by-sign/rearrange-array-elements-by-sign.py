class Solution:
    def rearrangeArray(self, nums):
        i = j = 0
        res = []

        while len(res) != len(nums):
            while i < len(nums)-1 and nums[i]<0:
                i+=1
            res.append(nums[i])
            i+=1
            
            while j < len(nums)-1 and nums[j] > 0:
                j+=1
            res.append(nums[j])
            j+=1
        
        return res

    

        