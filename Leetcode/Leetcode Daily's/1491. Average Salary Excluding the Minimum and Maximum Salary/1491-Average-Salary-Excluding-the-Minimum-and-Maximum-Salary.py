class Solution:
    def average(self, salary: list[int]) -> float:
        s = 0
        for x in salary:
            s += x
        
        s -= max(salary)
        s -= min(salary)

        s /= len(salary)-2
        
        return s