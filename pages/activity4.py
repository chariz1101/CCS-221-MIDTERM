import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.spatial import Delaunay

import tensorflow as tf

st.title("This is Activity 4")

tf.compat.v1.disable_eager_execution()

option=[] 
x=[]
y=[]
z=[]


def _cube_(bottom_lower=(0, 0, 0), side_length=3):
    """Create cube starting from the given bottom-lower point (lowest x, y, z values)"""
    bottom_lower = np.array(bottom_lower)
    
    points = np.vstack([
        bottom_lower,
        bottom_lower + [0, side_length, 0],
        bottom_lower + [side_length, side_length, 0],
        bottom_lower + [side_length, 0, 0],
        bottom_lower + [0, 0, side_length],
        bottom_lower + [0, side_length, side_length],
        bottom_lower + [side_length, side_length, side_length],
        bottom_lower + [side_length, 0, side_length],
        bottom_lower,
        
    ])   


    return points






def _plt_basic_object(points):
    """Plots a basic object, assuming its convex and not too complex"""
    
    tri = Delaunay(points).convex_hull
    
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111, projection='3d')
    S = ax.plot_trisurf(points[:,0], points[:,1],
                        points[:,2], triangles=tri,
                        shade=True, cmap=cm.rainbow,
                        lw=0.5
                        )
    
    ax.set_xlim3d(-5, 5)
    ax.set_ylim3d(-5, 5)
    ax.set_zlim3d(-5, 5)
    

    plt.show()
    st.pyplot (fig)
    
    
    
    
    
    
init_cube_ = _cube_(side_length=3)





def translate(points):
    def translate_obj(points, amount):
        return tf.add(points, amount)

    x = st.sidebar.slider('X Value', 0, 5)
    y = st.sidebar.slider('Y Value', 0, 5)
    z = st.sidebar.slider('Z Value', 0, 5)
    
    translation_amount = tf.constant([x, y, z], dtype=tf.float32)
    translated_shape = translate_obj(points, translation_amount)


    with tf.compat.v1.Session() as session:
 
            translated_shape = session.run(translated_shape)
            _plt_basic_object(translated_shape)        
            
            
            
def main():
    
    option = st.selectbox('What shape would you like to manipulate?', ('Cube', 'Pyramid', 'Rectangle', 'Diamond'))
    st.write('The shape you chose is:', option)
    
    if option == "Cube":
        
        
        
        option = st.selectbox('What form of manipulation will you use?', ('Translation', 'Rotation', 'Scaling', 'Shearing'))
        st.write('The shape you chose is:', option)
        
        if option == "Translation":
                        
            _cube_(bottom_lower=(0, 0, 0), side_length=3)
            init_cube_ = _cube_(side_length=3)
            points = tf.constant(init_cube_, dtype=tf.float32)
            st.subheader ('Translated Cube: ')
            translate(points)
            

if __name__ == '__main__':
    main()
