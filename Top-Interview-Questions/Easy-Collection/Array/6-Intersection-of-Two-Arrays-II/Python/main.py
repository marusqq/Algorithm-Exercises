class Solution:
    def intersect(self, nums1, nums2):
        intersecting_num = []
        
        if len(nums1) < len(nums2):
            cyclable_arr = nums1
            look_in = nums2
        else:
            cyclable_arr = nums2
            look_in = nums1
        
        i = 0
        while i < len(cyclable_arr):
            with_num = cyclable_arr[i] 
            if with_num in look_in: 
                intersecting_num.append(with_num)
                if len(cyclable_arr) == 1:
                    del cyclable_arr
                    break
                else:
                    cyclable_arr.remove(with_num)
                look_in.remove(with_num)
            else:
                i += 1

        return intersecting_num

ans = Solution()
n1 = [1,2,2,1]
n2 = [2,2]
print(ans.intersect(n1, n2))