class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def search(nums,target):
            arraySize = len(nums) - 1
            low = 0
            high = arraySize 
            result = high
            while low<=high:
                mid = low + (high - low)/2
                
                if nums[mid]<target:
                    low = mid + 1
                elif nums[mid]>target:
                    high = mid - 1
                else:
                    return mid
            return low
        return search(nums,target)
                    
        
