def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    l=[]
    r=[]
    for i in nums1:
        if i not in nums2:
            l.append(i)
    for i in nums2:
        if i not in nums1:
            r.append(i)
    return  l, r