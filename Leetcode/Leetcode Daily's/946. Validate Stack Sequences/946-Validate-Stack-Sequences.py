class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = [pushed[0]]
        n=1
        popped = collections.deque(popped)
        while popped:
            if not stack and not popped:
                return True
            if stack and popped[0]==stack[-1]:
                stack.pop()
                popped.popleft()
            
            elif n == len(pushed) and popped:
                return False

            else:
                stack.append(pushed[n])
                n+=1
        
        return True