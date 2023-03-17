import streamlit as st
import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt

fig = plt.figure()

def translation(i):
    
    #Translation
    m_translation_ = np.float32([[1, 0, 20],
                                 [0, 1, 10],
                                 [0, 0, 1]])
    
 
    image = cv2.imread(path + str(i) + png)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cols, rows = (image.shape[:2])

    translated_image = cv2.warpPerspective(image, m_translation_, (cols, rows))
    plt.axis('off')
    plt.imshow(translated_image)
    plt.show()
    st.pyplot(fig)

    
    
def rotation(images):
    angle = np.radians(10)
    m_rotation_ = np.float32([[np.cos(angle), -(np.sin(angle)), 0],
                              [np.sin(angle), np.cos(angle), 0],
                              [0, 0, 1]])
    
    rotated_image = cv2.warpPerspective(images, m_rotation_, (int(cols), int(rows)))
    plt.axis('off')
    plt.imshow(rotated_image)
    plt.show()
    st.pyplot(fig)
    
    
    
def scaling(images):
    m_scaling_ = np.float32([[1.5, 0, 0],
                             [0, 1.8, 0],
                             [0, 0, 1]])

    scaled_image = cv2.warpPerspective(images, m_scaling_, (cols*2, rows*2))
    plt.axis('off')
    plt.imshow(scaled_image)
    plt.show()
    st.pyplot(fig)
    
def shear(images,x,y):
    
    m_shearing_ = np.float32([[1, x, 0],
                               [y, 1, 0]])
   
    sheared_image = cv2.warpAffine(images, m_shearing_, (images.shape[1], images.shape[0]))
    plt.imshow(sheared_image)
    plt.show()
    st.pyplot(fig)

def reflection(images):
   
    m_reflection_ = np.float32([[1, 0, 0],
                                [0, -1, rows],
                                [0, 0, 1]])
    
  

    reflected_image = cv2.warpPerspective(images, m_reflection_,(int(cols), int(rows)))
    plt.imshow(reflected_image)
    plt.show()
    st.pyplot(fig)

    
def image_load():
    
    images = [] 
    address = []
    c = int(input('Enter number of files: '))
    for i in range(c):
        address.append(input(f'Upload Image {i + 1}/{c} : '))
    for path in address:
        images.append(cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB))
    return images
    
   
def main () :
    st.title('This is Activity 3')
    images = st.sidebar.file_uploader('Upload your files here', ['png', 'jpg', 'webp'], True)
        images = Image.open(images)
        images = np.asarray(images)
    option = st.sidebar.selectbox('What Image Manipulation Method to perform?', ('Translation', 'Rotation', 'Scaling', 'Shearing', 'Reflection'))
    st.write('The image manipulation you chose is:', option)
    
    if option == "Translation":
        st.write("Translation")
        translation(images)
    if option == "Rotation":
        st.write("Rotation")
        rotation(images)
    if option == "Scaling":
        st.write("Scale")
        scaling(images)
    if option == "Shearing":
        st.write("Shear")
        shear(images,x,y)
    if option == "Reflection":
        st.write("Reflection")
        reflection(images)
    
    
if __name__ == '__main__':
    main()
