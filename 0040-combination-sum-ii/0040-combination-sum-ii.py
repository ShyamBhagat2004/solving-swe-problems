class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        finalList, currList = [], []
        nums = candidates
        nums.sort()
        
        def dfs(i, currSum):
            if currSum == target:
                finalList.append(currList.copy())
                return None
            if currSum > target or i > len(nums)-1:
                return None
            
            
            #we want to keep this number
            currList.append(nums[i])
            dfs(i+1, currSum + nums[i])#<- this function
            currList.pop()
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i += 1
            #we don't want to keep this number anymore
            dfs(i+1, currSum)
            


        dfs(0, 0)
        finalList.sort()
        return finalList      