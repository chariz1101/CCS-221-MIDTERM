import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image

fig = plt.figure()


Bx_old = []
By_old = []
Tx = []
Ty = []


def translation(images, Bx_old, By_old):
    
    #Translation
    m_translation_ = np.float32([[1, 0, Bx_old],
                                 [0, 1, By_old],
                                 [0, 0, 1]])
    
 
    images = Image.open(images)
    images = np.asarray(images)
    cols, rows = images.shape[:2]

    translated_image = cv2.warpPerspective(images, m_translation_, (cols, rows))
    plt.axis('off')
    plt.imshow(translated_image)
    plt.show()
    st.pyplot(fig)


def translation_new(images, Bx_new,By_new):
    
    #Translation
    m_translation_ = np.float32([[1, 0, Bx_new],
                                 [0, 1, By_new],
                                 [0, 0, 1]])
    
 
    images = Image.open(images)
    images = np.asarray(images)
    cols, rows = images.shape[:2]

    translated_image = cv2.warpPerspective(images, m_translation_, (cols, rows))
    plt.axis('off')
    plt.imshow(translated_image)
    plt.show()
    st.pyplot(fig)


def main () :
 
    st.title ("This is Quiz 1: Image Translation Method ")
    st.write ("Upload Image first, then the Manipulation will appear.")
    filesUpload = st.sidebar.file_uploader('Upload image to manipulate: ', ['png', 'jpg', 'webp'], False)
    if filesUpload is not None:
        Bx_old = st.sidebar.slider(
            'Initial X',
            0, 100)


        By_old = st.sidebar.slider(
            'Initial Y',
            0, 100)


        Tx = st.sidebar.slider(
            'Added X',
            0, 300)


        Ty = st.sidebar.slider(
            'Added Y',
            0, 300)


        Bx_new = Bx_old + Tx
        By_new = By_old + Ty

        st.write('Original')
        translation(filesUpload, Bx_old, By_old)
        st.write('Translated')
        translation_new(filesUpload, Bx_new, By_new)

    
if __name__ == '__main__':
    main()
