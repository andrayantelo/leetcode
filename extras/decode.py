import collections
import timeit

class Solution:
    
    def helper(self, s, i, memo):
        answer = 0
        if memo[i]:
            return memo[i]
        if i >= len(s):
            memo[i] = 1
            answer += 1
            return 1
        
        if s[i] == '0':
            return 0
        
        nextDigit = self.helper(s, i+1, memo)
        memo[i+1] = nextDigit
        answer += nextDigit
        if i + 1 < len(s):
            nextDigit = self.helper(s, i + 2, memo)
            if s[i] == '1':
                memo[i + 2] = nextDigit
                answer += nextDigit
            if s[i] == '2' and i + 1 < len(s) and s[i+1] < '7':
                memo[i + 2] = nextDigit
                answer += nextDigit
        
        #print(memo)
        return answer
        
    """def noMemo(self, s, i):
        answer = 0
        if i >= len(s):
            answer += 1
            return 1
            
        if s[i] == '0':
            return 0
            
        
        answer += self.helper(s, i+1)
        if i + 1 < len(s):
            if s[i] == '1':
                answer += self.helper(s, i + 2)
            if s[i] == '2' and s[i + 1] < '7':
                answer += self.helper(s, i + 2)
            
        return answer"""
        
    
    def numDecodings(self, s):
        memo = collections.defaultdict(lambda: 0)
        return self.helper(s, 0, memo)
            
            
        
        
        
        
        
if __name__ == "__main__":
    solution = Solution()
    #print(timeit.timeit("solution.numDecodings("226")", setup="from __main__ import Solution"))
    print(solution.numDecodings("226"))
    print(solution.numDecodings("0"))
    print(solution.numDecodings("1"))
