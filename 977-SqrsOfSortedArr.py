class Solution(object):
    def sortedSquares(self, nums):
        def squares(nums):
            sqrd_nums = []
            for i in range(len(nums)):
                sqrd_nums.append(nums[i]*nums[i])
            #sort
            sqrd_nums.sort()
            return sqrd_nums
        return squares(nums)
          
    
        
