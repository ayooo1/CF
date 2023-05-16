class Solution:
    def minCostII(self, costs: list[list[int]]) -> int:
      n = len(costs)
      k = len(costs[0])
      dp = {}

      def dfs(idx,lastc):

        if idx == n:
          return 0
        
        if (idx,lastc) in dp:
          return dp[(idx,lastc)]
        
        best = float('inf')
        for i in range(k):
          if i != lastc:
            best = min(dfs(idx+1,i)+costs[idx][i],best)
        
        dp[(idx,lastc)] = best

        return best


      return dfs(0,-1) 