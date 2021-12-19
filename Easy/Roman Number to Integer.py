def romanToDecimal(str):
    # code here
    roman_1=['CM','CD','XC','XL','IX','IV']
    roman_2=['M','D','C','L','X','V','I']
    integer_1=[900,400,90,40,9,4]
    integer_2=[1000,500,100,50,10,5,1]
    ans=0
    for i in range(6):
        if roman_1[i] in str:
            ans+=integer_1[i]
            str=str.replace(roman_1[i],'')
    for j in str:
        ans+=integer_2[roman_2.index(j)]
        str=str.replace(j,'',1)
    return ans
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3




if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        print(romanToDecimal(str(input())))
# } Driver Code Ends