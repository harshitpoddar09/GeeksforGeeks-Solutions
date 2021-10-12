class Solution:
    def SubsequenceLength(self, s):
        #Codee here
        stack=[]
        ans=0
        for i in range(len(s)):
            if stack and s[i] in stack:
                ans=max(ans,len(stack))
                while s[i] in stack:
                    stack.pop(0)
            stack.append(s[i])
        ans=max(ans,len(stack))
        return ans
 
#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    s = input()
    print(Solution().SubsequenceLength(s))
    
# } Driver Code Ends