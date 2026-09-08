class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = nums
        def dfs(i,current,arr,ans):
            if i == len(arr):
                ans.append(list(current))
                return ans

            #take
            current.append(arr[i])
            dfs(i+1,current,arr,ans)
            current.pop()

            #skip
            dfs(i+1,current,arr,ans)

            # Return midlle calls
            return ans
        return dfs(0,[],arr,[])