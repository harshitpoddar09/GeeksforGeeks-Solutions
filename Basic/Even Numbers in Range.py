left,right=str(input()).split(',')
left=int(left)
right=int(right)
if left%2==0:
    for i in range(left,right+1,2):
        print(i,end=' ')
else:
    for i in range(left+1,right+1,2):
        print(i,end=' ')