import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

two_d_arr = np.array([[1, 0, 1],
                      [1, 0, 1],
                      [0, 1, 0]])

selected_color = 0
unselected_color = 0


def fill(x, y, replace, unselected_color):
    global two_d_arr

    for i in range(len(two_d_arr)):
        for j in range(len(two_d_arr[i])):
            if i == x and j == y:
                two_d_arr[x][y] = replace
            else:
                two_d_arr[i][j] = unselected_color

    fig = plt.figure()
    img = plt.imshow(two_d_arr, cmap='rainbow', interpolation='none')
    img.set_clim([1, 1000])
    plt.colorbar()
    plt.show()
    st.pyplot(fig)


def main():
    global selected_color
    global unselected_color

    st.title("This is Activity 2")

    x = st.sidebar.slider('y', 0, 2, 1)
    st.write('Value of X:', x)

    y = st.sidebar.slider('x', 0, 2, 1)
    st.write('Value of Y:', y)

    replace = st.sidebar.slider('Boundary Fill Color', 0, 1000, 500)
    st.write('Boundary Fill Color:', replace)

    selected_color = replace

    unselected_color = st.sidebar.slider('Flood Fill Color', 0, 1000, 0)
    st.write('Flood Fill Color:', unselected_color)

    fill(x, y, replace, selected_color, unselected_color)


if __name__ == '__main__':
    main()
