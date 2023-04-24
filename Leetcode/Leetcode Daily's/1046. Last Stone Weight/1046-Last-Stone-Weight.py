class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = []
        for i in stones:
            heap.append(-i)
        heapq.heapify(heap)
        ret = 0
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            print(x,y)

            if x == y:
                heapq.heappush(heap,0)
            else:
                heapq.heappush(heap,-(y-x))
        return -heap[0]
