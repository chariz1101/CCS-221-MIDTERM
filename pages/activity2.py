import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

two_d_arr = np.array([[1, 0, 1],
                      [1, 0, 1],
                      [0, 1, 0]])

def flood_fill(x, y, num_boxes, replace_color, boundary_color):
    rows, cols = two_d_arr.shape
    visited = set()
    stack = [(x, y)]

    while stack and num_boxes > 0:
        current_x, current_y = stack.pop()

        if (current_x, current_y) in visited:
            continue

        visited.add((current_x, current_y))

        if two_d_arr[current_x, current_y] == boundary_color:
            two_d_arr[current_x, current_y] = replace_color
            num_boxes -= 1

            neighbors = [
                (current_x - 1, current_y),
                (current_x + 1, current_y),
                (current_x, current_y - 1),
                (current_x, current_y + 1)
            ]

            for neighbor_x, neighbor_y in neighbors:
                if (
                    0 <= neighbor_x < rows and
                    0 <= neighbor_y < cols and
                    (neighbor_x, neighbor_y) not in visited
                ):
                    stack.append((neighbor_x, neighbor_y))

def main():
    st.title("This is Activity 2 and Flood Fill")

    activity_choice = st.sidebar.selectbox(
        "Select an activity",
        ("Boundary Fill", "Flood Fill")
    )

    if activity_choice == "Boundary Fill":
        x = st.sidebar.slider('y', 0, 2, 1)
        st.write('Value of X:', x)

        y = st.sidebar.slider('x', 0, 2, 1)
        st.write('Value of Y:', y)

        replace = st.sidebar.slider('color', 0, 1000, 500)
        st.write('color:', replace)

        for i in range(len(two_d_arr)):
            for j in range(len(two_d_arr[i])):
                if i == x and j == y:
                    two_d_arr[i, j] = replace

    elif activity_choice == "Flood Fill":
        x = st.sidebar.slider('y', 0, 2, 1)
        st.write('Value of X:', x)

        y = st.sidebar.slider('x', 0, 2, 1)
        st.write('Value of Y:', y)

        num_boxes = st.sidebar.slider('Number of Boxes', 1, 9, 1)
        replace = st.sidebar.slider('Color', 0, 1000, 500)
        st.write('Number of Boxes:', num_boxes)
        st.write('Color:', replace)

        flood_fill(x, y, num_boxes, replace, two_d_arr[x, y])

    fig = plt.figure()
    img = plt.imshow(two_d_arr, cmap='rainbow', interpolation='none')
    img.set_clim([1, 1000])
    plt.colorbar()
    plt.show()
    st.pyplot(fig)


if __name__ == '__main__':
    main()
