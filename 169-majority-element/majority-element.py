class Solution:
    def majorityElement(self, nums):
        maj = nums[0]
        count = 1
        i = 1
        while i <= len(nums)-1:
            if maj == nums[i]:
                count +=1
                maj = nums[i]
            else:
                if count == 0:
                    maj = nums[i]
                else:
                    count -= 1

            i+=1
        return maj
        