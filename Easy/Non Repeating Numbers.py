class Solution:
    def singleNumber(self, nums):
        # Code here
        ans=[]
        nums.sort()
        i=0
        while i<len(nums)-1:
            if nums[i]!=nums[i+1]:
                ans.append(nums[i])
                i+=1
            else:
                i+=2
        if len(ans)==1:
            ans.append(nums[-1])
        return ans


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        v = list(map(int,input().split()))
        ob = Solution();
        ans = ob.singleNumber(v)
        for i in ans:
            print(i, end = " ")
        print()

# } Driver Code Ends