import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # TC = (n log k) AND SC = O(k) -->heap never contains more than k elements
        # heappush → O(log k) AND  heappop → O(log k) 

        # create heap and store k
        # nums is simply the initial list of numbers.
        self.heap=[]
        self.k=k  

        # ti=o insert the existing nums[] in heap
        for num in nums:
            heapq.heappush(self.heap,num)

            if len(self.heap) > self.k:
                heapq.heappop(self.heap)      

    def add(self, val: int) -> int:
        # add val to heap
        # if heap becomes bigger than k, remove smallest
        # return kth largest

        # adding stream values to heap 

        heapq.heappush(self.heap,val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return (self.heap[0])
        
