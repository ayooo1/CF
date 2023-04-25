class SmallestInfiniteSet:

    def __init__(self):
        self.smallest = 1
        self.added = []
        self.added_set = set()

    def popSmallest(self) -> int:
        if self.added and self.added[0] < self.smallest:
            result = heapq.heappop(self.added)
            self.added_set.remove(result)
            return result
        result = self.smallest
        self.smallest += 1
        if self.added and self.smallest == self.added[0]:
            heapq.heappop(self.added)
            self.added_set.remove(self.smallest)
        return result

    def addBack(self, num: int) -> None:
        if num >= self.smallest or num in self.added_set:
            return
        heapq.heappush(self.added, num)
        self.added_set.add(num)
