def sort012(self,arr,n):
        # code here
        arr+=[0]*arr.count(0)
        arr+=[1]*arr.count(1)
        arr+=[2]*arr.count(2)
        del arr[:n]


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends