def find(arr,n,x):
    # code here
    ans=[-1,-1]
    if x in arr:
        ans[0]=arr.index(x)
        i=ans[0]
        while arr[i]==x:
            if i<n-1:
                i+=1
            else:
                ans[1]=i
                return ans
        ans[1]=i-1
        return ans
    return ans



#{ 
#  Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends