from typing import List

class MedianOfTwo():
    def getMedianOfSingleList(self, nums: List[int]) -> float:
        middleIndex = int(len(nums)/2)
        if len(nums) % 2 == 0:
            return (nums[middleIndex - 1] + nums[middleIndex]) / 2
        return nums[middleIndex]
        
    def combineLists(self, a: List[int], b: List[int]) -> List[int]:
        combinedNums = []
        while a and b:
            if a[0] < b[0]:
                combinedNums.append(a.pop(0))
            else:
                combinedNums.append(b.pop(0))
        while a:
            combinedNums.append(a.pop(0))
        while b:
            combinedNums.append(b.pop(0))
        return combinedNums
        
    def getMedian(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1: 
            return self.getMedianOfSingleList(nums2)
        if not nums2:
            return self.getMedianOfSingleList(nums1)
        return self.getMedianOfSingleList(self.combineLists(nums1, nums2))
        
        # middleIndex = int((m + n) / 2)
        # while i < m and j < n and nums1[i] < nums2[j] and i + j < middleIndex:
            # i += 1
        # i = min(i, m - 1)
        # while i < m and j < n and nums2[j] < nums1[i] and i + j < middleIndex:
            # j += 1
        # j = min(j, n - 1)
        # #print (nums1,',',nums2,':', i, ' ', nums1[i], ' ', j, ' ', nums2[j])
        # if (m + n) % 2 == 0:
            # return (nums1[i] + nums2[j]) / 2
        # return min(nums1[i], nums2[j])