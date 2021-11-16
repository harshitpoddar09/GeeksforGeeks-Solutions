"""
input - 
@s = given string 

output - 
return -1 or required ans
"""
class Solution:
    def missingPanagram(self, s):
        s=s.lower()
        a=set('qwertyuioplkjhgfdsazxcvbnm')
        for i in s:
            if i in a:
                a.remove(i)
        if len(a)==0:
            return -1
        return ''.join(sorted(a))


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        obj = Solution()
        print(obj.missingPanagram(s))
        t = t-1

# } Driver Code Ends