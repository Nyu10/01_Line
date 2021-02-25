from display import *

#this assignment took way too long for me, feeling mad stupid rn lol
def draw_line( x0, y0, x1, y1, screen, color ):
    x=int(x0)
    y=int(y0)
    A=y1-y0
    B=-(x1-x0)
    octant=what_octant(A,-B)
    if (octant==0):#horizontal
        if (-B>0):
            while(x<=x1):
                plot(screen,color,x,y)
                x+=1
        else:
            while(x>=x1):
                plot(screen,color,x,y)
                x-=1
    elif (octant==-1):#vertical
        if (A>0):
            while(y<=y1):
                plot(screen,color,x,y)
                y+=1
        else:
            while(y>=y1):
                plot(screen,color,x,y)
                y-=1
    #original algorithm
    elif (octant==1):
        d=2*A+B
        while(x<=x1):
            plot(screen,color,x,y)
            if (d>0):
                y+=1
                d+=2*B
            x+=1
            d+=2*A
    #interchange x and y
    elif (octant==2):
        d=A+2*B#use this for when y is greater
        while(y<=y1):
            plot(screen,color,x,y)
            if (d<0):
                x+=1
                d+=2*A
            y+=1 
            d+=2*B
    elif (octant==3):
        d=A-2*B
        while(y<=y1):
            plot(screen,color,x,y)
            if (d<0):
                x-=1
                d+=2*A
            y+=1 
            d+=2*-B
    elif (octant==4):
        d=2*A-B #changed to minus, B is moving faster
        while(x>=x1):
            plot(screen,color,x,y)
            if (d>0):
                y+=1
                d+=2*-B
            x-=1
            d+=2*A
    elif (octant==5):
        d=-2*A-B
        while(x>=x1):
            plot(screen,color,x,y)
            if (d<0):
                y-=1
                d+=2*B
            x-=1
            d+=2*A
    elif (octant==6):
        d=-A-2*B
        while(y>=y1):
            plot(screen,color,x,y)
            if (d>0):
                x-=1
                d+=2*A
            y-=1 
            d+=2*B
    elif (octant==7):
        d=-A+2*B
        while(y>=y1):
            plot(screen,color,x,y)
            if (d<0):
                x+=1
                d+=2*-A
            y-=1 
            d+=2*B
    elif (octant==8):
        d=-2*A+B
        while(x<=x1):
            plot(screen,color,x,y)
            if (d<0):
                y-=1
                d+=2*-B
            x+=1
            d+=2*A


def what_octant(A,B):
    if (A==0):
        return 0#horizontal
    elif (B==0):
        return -1#vertical
    elif (A>0):
        if (B>0):
            if (B>=A):#=
                return 1
            elif (B<A):
                return 2
        elif (B<0):#=
            if (A>-B):
                return 3
            elif(-B>A):
                return 4
    elif (A<0):
        if (B>0):
            if (B>=-A):#=
                return 8
            elif (B<-A):
                return 7
        elif (B<0):
            if (-A>-B):
                return 6
            elif(-B>-A):
                return 5
    
