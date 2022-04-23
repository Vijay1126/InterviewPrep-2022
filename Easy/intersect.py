class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if len(nums1) > len(nums2):
            # print("2")
            
            nums1, nums2 = nums2, nums1
        
        # print(nums1)
        nums1.sort()
        nums2.sort()
        index = 0
        i,j = 0, 0
        
        while i<len(nums1) and j<len(nums2):
            if nums1[i] == nums2[j]:
                print(nums1[i])
                nums1[index] = nums2[j]
                index+=1
                i+=1
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
            
        return nums1[:index]
