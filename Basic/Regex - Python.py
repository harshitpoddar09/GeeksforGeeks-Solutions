#Driver Code Starts
#Initial Template for Python 3


import re ##import re module to use regex

 # } Driver Code Ends
#User function Template for python3



def numberMatcher(str):
    pat=re.compile(r'\d+') #write the pattern here
    match=re.findall(pat,str) #find all finds all the matched texts and returns a list
    if(match): 
        for i in match:
            print(i, end=" ")
    else:
        print(-1,end="")


#{ 
#Driver Code Starts.

def main():
    testcases = int(input()) #testcases
    while(testcases > 0):
        str = input()
        numberMatcher(str)
        print()
        testcases -= 1
        


if __name__=='__main__':
    main()
#} Driver Code Ends