#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3

def cat_hat(str):
  ##your code here##
  ##You need to write complete code this time 
    cat=0
    hat=0
    while 'cat' in str:
        str=str.replace('cat','',1)
        cat+=1
    while 'hat' in str:
        str=str.replace('hat','',1)
        hat+=1
    return cat==hat


#{ 
#Driver Code Starts.




def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        str = input()
        print(cat_hat(str))
        testcases-=1
        


if __name__=='__main__':
    main()
#} Driver Code Ends