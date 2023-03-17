import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt

png = str(".png")
fig = plt.figure()
path = str("pages/")
i = 1

Bx_old = []
By_old = []
Tx = []
Ty = []


def translation(Bx_old, By_old):
    
    #Translation
    m_translation_ = np.float32([[1, 0, Bx_old],
                                 [0, 1, By_old],
                                 [0, 0, 1]])
    
 
    image = cv2.imread(path + str(i) + png)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cols, rows = (image.shape[:2])

    translated_image = cv2.warpPerspective(image, m_translation_, (cols, rows))
    plt.axis('off')
    plt.imshow(translated_image)
    plt.show()
    st.pyplot(fig)


def translation_new(Bx_new,By_new):
    
    #Translation
    m_translation_ = np.float32([[1, 0, Bx_new],
                                 [0, 1, By_new],
                                 [0, 0, 1]])
    
 
    image = cv2.imread(path + str(i) + png)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cols, rows = (image.shape[:2])

    translated_image = cv2.warpPerspective(image, m_translation_, (cols, rows))
    plt.axis('off')
    plt.imshow(translated_image)
    plt.show()
    st.pyplot(fig)


def main () :
  

    st.title('Quiz')
    
    Bx_old = st.sidebar.slider(
        'Initial X',
        0, 1000)


    By_old = st.sidebar.slider(
        'Initial Y',
        0, 1000)


    Tx = st.sidebar.slider(
        'Added X',
        0, 1000)


    Ty = st.sidebar.slider(
        'Added Y',
        0, 1000)


    Bx_new = Bx_old + Tx
    By_new = By_old + Ty
    
    st.write('Original')
    translation(Bx_old, By_old)
    st.write('Translated')
    translation_new(Bx_new, By_new)

    
if __name__ == '__main__':
    main()
