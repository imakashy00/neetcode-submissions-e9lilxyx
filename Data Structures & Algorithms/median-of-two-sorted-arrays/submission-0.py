class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_array:list[int] = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                new_array.append(nums1[i])
                i+=1
            else:
                new_array.append(nums2[j])
                j+=1
        while i < len(nums1):
            new_array.append(nums1[i])
            i+=1
        while j < len(nums2):
            new_array.append(nums2[j])
            j+=1
        if len(new_array) & 1:
            return new_array[(len(new_array)//2)]
        else:
            return (new_array[(len(new_array)//2)-1] + new_array[(len(new_array)//2)])/2