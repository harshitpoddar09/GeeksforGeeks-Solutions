x1,y1=str(input()).split(',')
x2,y2=str(input()).split(',')
x,y=str(input()).split(',')
x1=int(x1)
x2=int(x2)
x=int(x)
y1=int(y1)
y2=int(y2)
y=int(y)
if x>x1 and x<x2 and y>y1 and y<y2:
    print(1)
else:
    print(0)