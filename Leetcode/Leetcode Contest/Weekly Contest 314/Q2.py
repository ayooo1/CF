'''

here just want to xor everything from the prev index
thats why we start at index 1 and go the to end

'''
class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        arr = [pref[0]]
        for i in range(1,len(pref)):
            arr.append(pref[i-1]^pref[i])
        return arr