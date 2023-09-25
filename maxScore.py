def maxScore(nums1 ,nums2, k) :
    import heapq
    ans = 0
    summ = 0
    # (nums2[i], nums1[i]) sorted by nums2[i] in descending order.
    A = sorted([(num2, num1)
                for num1, num2 in zip(nums1, nums2)], reverse=True)
    minHeap = []
    for num2, num1 in A:
        heapq.heappush(minHeap, num1)
        summ += num1
        if len(minHeap) > k:
            summ -= heapq.heappop(minHeap)
        if len(minHeap) == k:
            ans = max(ans, summ * num2)
        print(num1,num2,minHeap,summ)
    return A