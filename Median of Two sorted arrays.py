class Solution:
    
    #Function to find the median of the two arrays when they get merged.
    def findMedianSortedArrays(self,arr1, n, arr2, n2):
       
        #code here
        total_len=n+n2
        i=0
        j=0
        idx=0
        while i<n and j<n2:
            if arr1[i]<arr2[j]:
                i+=1
            else:
                j+=1
            if idx==(total_len//2)-2:
                break
            idx+=1
        a=0
        b=0
        if idx==(total_len//2)-2:
            if i<n and j<n2:
                if arr1[i]<arr2[j]:
                    a=arr1[i]
                    i+=1
                    if i<n and arr1[i]<arr2[j]:
                        b=arr1[i]
                    else:
                        b=arr2[j]
                else:
                    a=arr2[j]
                    j+=1
                    if j<n2 and arr1[i]>arr2[j]:
                        b=arr2[j]
                    else:
                        b=arr1[i]
            elif i<n:
                a=arr1[i]
                b=arr1[i+1]
            else:
                a=arr2[j]
                b=arr2[j+1]
        else:
            while i<n:
                i+=1
                if idx==(total_len//2)-2:
                    break
                idx+=1
            while j<n2:
                j+=1
                if idx==(total_len//2)-2:
                    break
                idx+=1
            if i<n:
                a=arr1[i]
                b=arr1[i+1]
            else:
                a=arr2[j]
                b=arr2[j+1]
        if total_len%2==0:
            return (a+b)//2
        else:
            return b

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n1,n2=list(map(int,(input().split())))
        arr1=list(map(int,(input().split())))
        arr2=list(map(int,(input().split())))
        
        if n1<n2:
            print(Solution().findMedianSortedArrays(arr1,n1, arr2,n2))
        else:
            print(Solution().findMedianSortedArrays(arr2,n2, arr1,n1))
# } Driver Code Ends