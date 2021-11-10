#User function Template for python3

class Solution:
    
    #Function to find the maximum occurring character in a string.
    def getMaxOccurringChar(self,s):
        #code here
        s=''.join(sorted(list(s)))
        idx=0
        cur_occur=1
        max_occur=1
        i=1
        while i<len(s):
            if s[i]==s[i-1]:
                cur_occur+=1
            else:
                cur_occur=1
            if cur_occur>max_occur:
                max_occur=cur_occur
                idx=i
            i+=1
        return s[idx]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        print(Solution().getMaxOccurringChar(s))
# } Driver Code Ends