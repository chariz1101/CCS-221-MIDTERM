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
choice=[]
w=[] 
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

    x = st.sidebar.slider('X Value', -5, 5, 0)
    y = st.sidebar.slider('Y Value', -5, 5, 0)
    z = st.sidebar.slider('Z Value', -5, 5, 0)
    
    translation_amount = tf.constant([x, z, y], dtype=tf.float32)
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
            x = st.sidebar.slider('Angle', 0, 100, 0)
            rotated_object = session.run(rotate_obj(init_cube_, x)) 
            _plt_basic_object(rotated_object)
            
        if option == "Pyramid":
            x = st.sidebar.slider('Angle', 0, 100, 0)
            rotated_object = session.run(rotate_obj(init_pyramid_, x)) 
            _plt_basic_object(rotated_object)
            
        if option == "Rectangle":
            x = st.sidebar.slider('Angle', 0, 100, 0)
            rotated_object = session.run(rotate_obj(init_rectangle_, x)) 
            _plt_basic_object(rotated_object)
            
        if option == "Diamond":
            x = st.sidebar.slider('Angle', 0, 100, 0)
            rotated_object = session.run(rotate_obj(init_diamond_, x)) 
            _plt_basic_object(rotated_object)   




def scale(points):
    def scale_obj(points, amount):
        return tf.multiply(points, amount)

    x = st.sidebar.slider('X Value', -5, 5, 1)
    y = st.sidebar.slider('Y Value', -5, 5, 1)
    z = st.sidebar.slider('Z Value', -5, 5, 1)

    scale_amount = tf.constant([x,z,y], dtype=tf.float32)
    scaled_object = scale_obj(points, scale_amount)

    with tf.compat.v1.Session() as session:
         scaled_cube = session.run(scaled_object)
    
    _plt_basic_object(scaled_cube)






def shear_y(points):

    def shear_obj_y(points, yold, ynew, zold, znew):
  
        sh_y = tf.multiply(yold, ynew)
        sh_z = tf.multiply(zold, znew)
        
        shear_points = tf.stack([
                                [sh_y, 0, 0],
                                [sh_z, 1, 0,],
                                [0, 0, 1]
                                ])
        
        shear_object = tf.matmul(tf.cast(points, tf.float32), tf.cast(shear_points, tf.float32))
        return shear_object
    
    with tf.compat.v1.Session() as session:
        w = st.sidebar.slider('Y Old', -5.0, 5.0, 1.0)
        x = st.sidebar.slider('Y New', -5.0, 5.0, 1.0)
        y = st.sidebar.slider('Z Old', -5.0, 5.0, 0.0)
        z = st.sidebar.slider('Z New', -5.0, 5.0, 0.0)
        sheared_object_y = session.run(shear_obj_y(points, w, x, y, z))
    
    _plt_basic_object(sheared_object_y)
    
    
    
 
 
 
def shear_x(points):   
    
    def shear_obj_x(points, xold, xnew, zold, znew):
        
        sh_x = tf.multiply(xold, xnew)
        sh_z = tf.multiply(zold, znew)
        
        shear_points = tf.stack([
                                [1, sh_x, 0],
                                [0, 1, 0,],
                                [0, sh_z, 1]
                                ])
        
        shear_object = tf.matmul(tf.cast(points, tf.float32), tf.cast(shear_points, tf.float32))
        return shear_object
    
    with tf.compat.v1.Session() as session:
        w = st.sidebar.slider('X Old', -5.0, 5.0, 0.0)
        x = st.sidebar.slider('X New', -5.0, 5.0, 0.0)
        y = st.sidebar.slider('Z Old', -5.0, 5.0, 0.0)
        z = st.sidebar.slider('Z New', -5.0, 5.0, 0.0)
        sheared_object_x = session.run(shear_obj_x(points, w, x, y, z))
    
    _plt_basic_object(sheared_object_x)
    
    
    
    
    






    
            
def main():
    
    option = st.sidebar.selectbox('What shape would you like to manipulate?', ('Cube', 'Pyramid', 'Rectangle', 'Diamond'))
    st.write('The shape you chose is:', option)
    
    if option == "Cube":
        choice = st.sidebar.selectbox('What form of manipulation will you use?', ('Translation', 'Rotation', 'Scaling', 'Shearing'))
        st.write('The shape you chose is:', choice)
        
        _cube_(bottom_lower=(0, 0, 0), side_length=3)
        init_cube_ = _cube_(side_length=3)
        points = tf.constant(init_cube_, dtype=tf.float32)
            
        if choice == "Translation":
            st.subheader ('Translated Cube: ')
            translate(points)
                
        if choice == "Rotation":
            st.subheader ('Rotated Cube: ')
            rotate(option, points)

        if choice == "Scaling":
            st.subheader ('Scaled Cube: ')
            scale(points)

        if choice == "Shearing":
            option = st.sidebar.selectbox('Type of Shear', ('Shear X', 'Shear Y'))
            
            if option == "Shear Y":
                    st.subheader ('Sheared Cube: ')
                    shear_y(points)
                    
            if option == "Shear X":
                    st.subheader ('Sheared Cube: ')
                    shear_x(points)
        
    
    
    if option == "Pyramid":
        choice = st.sidebar.selectbox('What form of manipulation will you use?', ('Translation', 'Rotation', 'Scaling', 'Shearing'))
        st.write('The shape you chose is:', choice)
        
        _pyramid_(side_length=1)
        init_pyramid_ = _pyramid_(side_length=1)
        points = tf.constant(init_pyramid_, dtype=tf.float32)
            
        if choice == "Translation":
            st.subheader ('Translated Pyramid: ')
            translate(points)
                
        if choice == "Rotation":
            st.subheader ('Rotated Pyramid: ')
            rotate(option, points)

        if choice == "Scaling":
            st.subheader ('Scaled Pyramid: ')
            scale(points)

        if choice == "Shearing":
            option = st.sidebar.selectbox('Type of Shear', ('Shear X', 'Shear Y'))
            
            if option == "Shear Y":
                    st.subheader ('Sheared Pyramid: ')
                    shear_y(points)
                    
            if option == "Shear X":
                    st.subheader ('Sheared Pyramid: ')
                    shear_x(points)
        

if __name__ == '__main__':
    main()
