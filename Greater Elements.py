#Given 2 arrays of numbers, where the first array is a subset of the second array,
# return an array containing all the next greater elements for each element in the first array
#if there is no greater element, return -1

def greater_elements(nums1, nums2):
    nums1len = len(nums1)
    nums2len = len(nums2)
    ans = []
    for i in range(nums1len):
        ans.append(-1)
        for j in range(nums2len):
            if nums2[j] > nums1[i]:
                ans[i] = nums2[j]
                break
    print (ans)









# nums1 = [4, 1, 2]
# nums2 = [1, 3, 4, 2]
#
nums1 = [2, 4]
nums2 = [1, 2, 3, 4]

greater_elements(nums1, nums2)