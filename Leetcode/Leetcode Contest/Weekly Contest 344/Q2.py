from collections import defaultdict


class FrequencyTracker:

    def __init__(self):
        self.lst = defaultdict(int)
        self.freq = defaultdict(int)
        

    def add(self, number: int) -> None:
        self.lst[number]+=1
        self.freq[self.lst[number]] += 1
        if self.lst[number]-1 > 0 and self.freq[self.lst[number]-1] > 0:
            self.freq[self.lst[number]-1] -= 1
        

    def deleteOne(self, number: int) -> None:
        if not self.lst[number]:
            return
        self.lst[number] -= 1
        self.freq[self.lst[number]] += 1
        
        if self.freq[self.lst[number]+1] >= 1:
            self.freq[self.lst[number]+1] -= 1
        

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)