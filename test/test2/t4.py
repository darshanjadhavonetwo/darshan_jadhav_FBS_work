h=int(input("enter the  hight of wall:"))
w=int(input("enter the width of wall:"))
cs=int(input("enter the painting cost per square foot:"))
if(h>0 and w>0 and cs>0):
    a=h*w
    t_a=4*a
    t_c=t_a*cs
    print(f"{t_c}: it is total cost of paintitng the interior wall")
else:
    print(".")