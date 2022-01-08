# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        low = 1
        high = n
        result = high
        while(low<=high):
            mid = (low+high)//2
            if isBadVersion(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result
        
