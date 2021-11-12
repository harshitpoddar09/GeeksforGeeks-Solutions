#Your function should return a String
def convertRoman(n):
    #Code here
    num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    roman = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    i=12
    ans=''
    while n:
        qou=n//num[i]
        n%=num[i]
        ans+=roman[i]*qou
        i-=1
    return ans

#{ 
#  Driver Code Starts
#Your Code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(convertRoman(n))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends