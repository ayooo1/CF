class Solution:
    def countSeniors(self, details: list[str]) -> int:
        c = 0
        for detail in details:
            if int(detail[11:13]) > 60:
                c += 1
        return c