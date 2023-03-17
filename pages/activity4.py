

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
def _pyramid_(side_length=1):

    points = np.vstack([
            ([[-1, -1, -1],
                [side_length, -1, -1 ],
                [side_length, side_length, -1],
                [-1, side_length, -1],
                [0, 0 , side_length]])
    ])        
         
    return points



def _rectangle_(bottom_lower=(0, 0, 0), side_length=2):
    """Create cube starting from the given bottom-lower point (lowest x, y, z values)"""
    bottom_lower = np.array(bottom_lower)
    
    points = np.vstack([
        bottom_lower,
        [side_length, 0, 0],
        [side_length, 4, 0],
        [0, 4, 0],
        [0, 0, 3],
        [side_length, 0, 3],
        [side_length, 4, 3],
        [0, 4, 3]
    ])   
    
    return points



def _diamond_(side_length=1):

    points = np.vstack([
                ([[-1, -1, -1],
                [side_length, -1, -1 ],
                [side_length, side_length, -1],
                [-1, side_length, -1],
                [0, 0 , side_length],
                [0, 0, -3]
                ])
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
init_pyramid_ = _pyramid_(side_length=1)
init_rectangle_ = _rectangle_(side_length=3)
init_diamond_ = _diamond_(side_length=1)

def translate(points):
    def translate_obj(points, amount):
        return tf.add(points, amount)


    translation_amount = tf.constant([1, 2, 2], dtype=tf.float32)
    translated_shape = translate_obj(points, translation_amount)


    with tf.compat.v1.Session() as session:
 
            translated_shape = session.run(translated_shape)
            _plt_basic_object(translated_shape)       
            

def rotate(option, points):
    def rotate_obj(points, angle):
        angle = float(angle)
        rotation_matrix = tf.stack([
                        [tf.cos(angle), tf.sin(angle), 0],
                        [-tf.sin(angle), tf.cos(angle), 0],
                        [0, 0, 1]
        ])

        rotate_object = tf.matmul(tf.cast(points, tf.float32), tf.cast(rotation_matrix, tf.float32))
        
        return rotate_object
        
        
    with tf.compat.v1.Session() as session:
            
        if option == "Cube":
            rotated_object = session.run(rotate_obj(init_cube_, 75)) 
            _plt_basic_object(rotated_object)
            
        if option == "Pyramid":
            rotated_object = session.run(rotate_obj(init_pyramid_, 75)) 
            _plt_basic_object(rotated_object)
            
        if option == "Rectangle":
            rotated_object = session.run(rotate_obj(init_rectangle_, 75)) 
            _plt_basic_object(rotated_object)
            
        if option == "Diamond":
            rotated_object = session.run(rotate_obj(init_diamond_, 75)) 
            _plt_basic_object(rotated_object)        
            
def main():
    
    option = st.selectbox('What shape would you like to manipulate?', ('Cube', 'Pyramid', 'Rectangle', 'Diamond'))
    st.write('The shape you chose is:', option)
    if option == "Cube":
        _cube_(bottom_lower=(0, 0, 0), side_length=3)
        init_cube_ = _cube_(side_length=3)
        points = tf.constant(init_cube_, dtype=tf.float32)
        st.subheader ('Translated Cube: ')
        translate(points)
        st.subheader ('Cube rotated 75 Degrees: ')
        rotate(option, points)
        
    if option == "Pyramid":
        _pyramid_(side_length=1)
        init_pyramid_ = _pyramid_(side_length=1)
        points = tf.constant(init_pyramid_, dtype=tf.float32)
        st.subheader ('Translated Pyramid: ')
        translate(points)
        st.subheader ('Pyramid rotated 75 Degrees: ')
        rotate(option, points)
            
    if option == "Rectangle":
        _rectangle_(side_length=3)
        init_pyramid_ = _rectangle_(side_length=3)
        points = tf.constant(init_rectangle_, dtype=tf.float32)
        st.subheader ('Translated Rectangle: ')
        translate(points)
        st.subheader ('Rectangle rotated 75 Degrees: ')
        rotate(option, points)
            
    if option == "Diamond":
        _diamond_(side_length=1)
        init_pyramid_ = _diamond_(side_length=1)
        points = tf.constant(init_diamond_, dtype=tf.float32)
        st.subheader ('Translated Diamond: ')
        translate(points)
        st.subheader ('Diamond rotated 75 Degrees: ')
        rotate(option, points)
        
if __name__ == '__main__':
    main()
