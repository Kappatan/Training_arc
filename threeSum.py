def threeSum( nums) :
    # l=[]
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         for k in range(0, i):
    #             if nums[i] + nums[j] + nums[k] == 0:
    #                 a = [nums[i], nums[j], nums[k]]
    #                 a.sort()
    #                 if a not in l:
    #                     l.append(a)
    #
    # return l
    triplets = []
    for i in range(len(nums)):
        target = -(nums[i])
        d = {}
        for j in range(i + 1, len(nums)):
            if target - nums[j] in d:
                triplets.append(sorted([nums[i], target - nums[j], nums[j]]))
            else:
                d[nums[j]] = j
    return sorted(list(set(map(tuple,triplets))))

print(threeSum(nums = [-1,0,1,2,-1,-4]))