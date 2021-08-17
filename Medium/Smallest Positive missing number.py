class Solution:
    def findMissing(self,arr, size): 
    # your code goes here
        arr.sort()
        if size==0 or max(arr)<=0:
            return 1
        i=1
        j=0
        while i<size+2 and j<size:
            while j<size and arr[j]<i:
                j+=1
            if arr[j]==i:
                i+=1
                j+=1
            elif arr[j]!=i:
                return i
        return size+1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.findMissing(arr, n))
# } Driver Code Ends