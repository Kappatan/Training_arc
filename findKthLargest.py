def findKthLargest(nums, k) :
    max_heap = []
    import heapq
    for num in nums:
        # Push the negative of the current element onto the max heap
        heapq.heappush(max_heap, num)
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    return max_heap[0]