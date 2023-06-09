import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image

fig = plt.figure()

def translation(images, x, y):
    m_translation_ = np.float32([[1, 0, x],
                                 [0, 1, y],
                                 [0, 0, 1]])
    
    
    images = Image.open(images)
    images = np.asarray(images)
    cols, rows = images.shape[:2]
    translated_image = cv2.warpPerspective(images, m_translation_, (int(cols), int(rows)))
    plt.axis('off')
    plt.imshow(translated_image)
    plt.show()
    st.pyplot(fig)

def rotation(images, angle):
    angle = np.radians(angle)
    m_rotation_ = np.float32([[np.cos(angle), -(np.sin(angle)), 0],
                              [np.sin(angle), np.cos(angle), 0],
                              [0, 0, 1]])
    
   
    images = Image.open(images)
    images = np.asarray(images) 
    cols, rows = images.shape[:2]
    rotated_image = cv2.warpPerspective(images, m_rotation_, (int(cols), int(rows)))
    plt.axis('off')
    plt.imshow(rotated_image)
    plt.show()
    st.pyplot(fig)
    
def scaling(images,scalex,scaley):
    m_scaling_ = np.float32([[scalex, 0, 0],
                             [0, scaley, 0],
                             [0, 0, 1]])
    
   
    images = Image.open(images)
    images = np.asarray(images)
    cols, rows = images.shape[:2]
    scaled_image = cv2.warpPerspective(images, m_scaling_, (cols*2, rows*2))
    plt.axis('off')
    plt.imshow(scaled_image)
    plt.show()
    st.pyplot(fig)
    
def shear(images,x, y):
    m_shearing_ = np.float32([[1, x, 0],
                               [y, 1, 0],
                               [0, 0, 1]])
    
    
    images = Image.open(images)
    images = np.asarray(images)
    cols, rows = images.shape[:2]
    sheared_image = cv2.warpPerspective(images, m_shearing_,(int(cols*1.5), int(rows*1.5)))
    plt.axis('off')
    plt.imshow(sheared_image)
    plt.show()
    st.pyplot(fig)

def reflection(images):
    images = Image.open(images)
    images = np.asarray(images)
    cols, rows = images.shape[:2] 
    st.sidebar.write('Flip Option:')    
    choice = st.sidebar.selectbox('Image Position', ('Base Image', 'Vertical Flip', 'Horizontal Flip'))
    
    if choice == "Base Image":
        m_reflection_ = np.float32([[1, 0, 0],
                                    [0, 1, 0],
                                    [0, 0, 1]])
        
        
    elif choice == "Vertical Flip":
        m_reflection_ = np.float32([[1, 0, 0],
                                    [0, -1, rows],
                                    [0, 0, 1]])

        
    elif choice == "Horizontal Flip":
        m_reflection_ = np.float32([[-1, 0, cols],
                                    [0, 1, 0],
                                    [0, 0, 1]])
   

    reflected_image = cv2.warpPerspective(images, m_reflection_,(int(cols), int(rows)))
    plt.axis('off')
    plt.imshow(reflected_image)
    plt.show()
    st.pyplot(fig)

def main():
    st.title ("This is Activity 3: Image Manipulation Methods ")
    st.write ("Upload Image first, then the Manipulation will appear.")
    filesUpload = st.sidebar.file_uploader('Upload image to manipulate: ', ['png', 'jpg', 'webp'], False)
    if filesUpload is not None:
        option = st.sidebar.selectbox('What Image Manipulation Method to perform?', ('Translation', 'Rotation', 'Scaling', 'Shearing', 'Reflection'))
        st.write('The image manipulation you chose is:', option)

        if option == "Translation":
           x = st.sidebar.slider('X Translation', 0.0, 300.0, 0.1)
           y = st.sidebar.slider('Y Translation', 0.0, 300.0, 0.1)
           translation(filesUpload, x, y)

        if option == "Rotation":
            angle = st.sidebar.slider('Rotation Degrees', -90.0, 90.0, 0.1)
            st.write("Rotation")
            rotation(filesUpload, angle)

        if option == "Scaling":
            scalex = st.sidebar.slider('X Coordiante: ', 0.0, 10.0, 0.1)
            scaley = st.sidebar.slider('Y Coordinate: ', 0.0, 10.0, 0.1)
            st.write("Scale")
            scaling(filesUpload, scalex, scaley)

        if option == "Shearing":
            st.write("Shear")
            x = st.sidebar.slider('X Coordinate: ', 0.0, 10.0, 0.1)
            y = st.sidebar.slider('Y Coordinate: ', 0.0, 10.0, 0.1)
            shear(filesUpload,x,y)

        if option == "Reflection":
            st.write("Reflection")
            reflection(filesUpload)

if __name__ == '__main__':
    main()
