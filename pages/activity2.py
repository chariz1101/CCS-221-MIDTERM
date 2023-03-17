import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import altair as alt

two_d_arr = np.array([[1, 0, 1],
                      [1, 0, 1],
                      [0, 1, 0]])
    
x = []
y = []
replace = []
    
def fill(x, y, replace):
    
    for i in range(len(two_d_arr)):
        for j in range(len(two_d_arr[i])):
            two_d_arr[x][y] = replace
    
    fig = plt.figure ()
    img = plt.imshow(two_d_arr, cmap='rainbow', interpolation='none')
    img.set_clim([1,1000])
    plt.colorbar()
    plt.show()
    st.pyplot (fig)
    

    
def main():
   st.title("This is Activity 2")

   x = st.sidebar.slider('y',0, 2, 1)
   st.write('Value of X:', x)
    
   y = st.sidebar.slider('x',0, 2, 1)
   st.write('Value of Y:', y)
    
   replace = st.sidebar.slider('color',0, 1000, 500)
   st.write('color:', replace)
    
   fill(x, y, replace)

  
  
  
if __name__ == '__main__':
  main()
