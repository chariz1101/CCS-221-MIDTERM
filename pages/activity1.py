import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import altair as alt



def DDALine(x1, y1, x2, y2, color):
    dx = y2 - x1
    dy = y2 - y1
    mpx = (x1 + x2) / 2         #midpoint
    mpy = (y1 + y2) / 2         #midpoint

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    Xinc = float(dx/steps)
    Yinc = float(dy/steps)

    fig = plt.figure()
    for i in range(0, int(steps +1)):
            plt.plot(int(x1), int(y1), color)
            x1 += Xinc
            y1 += Yinc
            

    st.write('[DDA Line] Midpoint of the line is (x,y): ', mpx, mpy)

    plt.show() 
    st.pyplot(fig)

        




def bresenham(x1, y1, x2, y2, color): 
   
 
    dx = abs(x2 - x1) #change in x / delta x
    dy = abs(y2 - y1) #change in y / delta y
    mpx = (x1 + x2) / 2 #x midpoint
    mpy = (y1 + y2) / 2 #y midpoint

    slope = dy/float(dx) #slope
    
    if slope > 1:
        dx, dy = dy, dx
        x1, y1 = y1, x1
        x2 ,y2 = y2, x2

    pk = 2 * dy - dx #decision parameter
    
    xcoords = [x1] #x-coordinates
    ycoords =[y1] #y-coordinates
   
    fig2=plt.figure()
    for x in range(2,dx):
        
        if pk > 0: #case 2 [decision parameter satisfied] 
            y1 = y1 + 1 if y1 < y2 else y1 - 1
            pk = pk + 2 * (dy - dx)
            
        else : #otherwise
            pk = pk + 2 * dy
        
        
        x1 = x1 + 1 if x1 < x2 else x1 - 1
        
        
        xcoords.append(x1)
        ycoords.append(y1)

    st.write('[Bresenhams Line] Midpoint of the Line is (x,y): ', mpx, mpy)


    plt.plot(xcoords,ycoords)
    plt.show() 
    st.pyplot(fig2)
    
    
    
    
    
    
def midpoint(x1, y1, x2, y2, color): 
   
    x, y = x1, y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    x3 = (x1 + x2) / 2
    y3 = (y1 + y2) / 2

    slope = dy/float(dx)
    
    if slope > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2 ,y2 = y2, x2

    p = 2 * dy - dx
    
    xcords = [x]
    ycords =[y]
   
    fig3=plt.figure()
    for k in range(2,dx):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else :
            p = p + 2 * dy
        
        x = x + 1 if x < x2 else x - 1
        
        xcords.append(x)
        ycords.append(y)

    st.write('Midpoint of the line is:', x3)
    plt.plot(xcords,ycords,x3,y3,marker="o",markersize=5,markerfacecolor="red")
    plt.show()
    st.pyplot(fig3)
    
    
    

def main(): 
    st.title("This is Activity 1")
    option = st.sidebar.selectbox('What Type of Line to Perform?', ('DDA Line', 'Bresenham', 'Midpoint'))
    st.write('The type of line you chose is:', option)
    if option == "DDALine":
        DDALine(x, y, xEnd, yEnd, color)

    if option == "bresenham":
        bresenham(x,y,xEnd, yEnd, color) # call for Bresenham's Line function

    if option == "midpoint":
        midpoint(x,y,xEnd, yEnd, color)



    x = st.sidebar.slider(
        'X1',
        1, 1000)
    st.write('Value of X1: ', x)

    y = st.sidebar.slider(
        'Y1',
        1, 1000)
    st.write('Value of Y1: ', y)

    xEnd = st.sidebar.slider(
        'X2',
        0, 1000)
    st.write('Value of X2: ', xEnd)

    yEnd = st.sidebar.slider(
        'Y2',
        0, 1000)
    st.write('Value of Y2: ', yEnd)
    color = "b." 


if __name__ == '__main__':
    main()    
