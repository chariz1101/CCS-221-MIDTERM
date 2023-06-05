import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

two_d_arr = np.array([[1, 0, 1],
                      [1, 0, 1],
                      [0, 1, 0]])

def flood_fill(x, y, replace, boundary_color):
    rows, cols = two_d_arr.shape
    visited = set()
    stack = [(x, y)]

    while stack:
        current_x, current_y = stack.pop()

        if (current_x, current_y) in visited:
            continue

        visited.add((current_x, current_y))

        if two_d_arr[current_x, current_y] == boundary_color:
            two_d_arr[current_x, current_y] = replace

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

def move_box(x, y, new_x, new_y):
    rows, cols = two_d_arr.shape

    if 0 <= x < rows and 0 <= y < cols:
        value = two_d_arr[x, y]
        two_d_arr[x, y] = 0

        if 0 <= new_x < rows and 0 <= new_y < cols:
            two_d_arr[new_x, new_y] = value

def main():
    st.title("This is Activity 2")

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
        replace = st.sidebar.slider('replace', 0, 1000, 500)
        st.write('replace:', replace)

        x = st.sidebar.slider('box x', 0, 2, 1)
        st.write('Box X:', x)

        y = st.sidebar.slider('box y', 0, 2, 1)
        st.write('Box Y:', y)

        new_x = st.sidebar.slider('new x', 0, 2, 1)
        st.write('New X:', new_x)

        new_y = st.sidebar.slider('new y', 0, 2, 1)
        st.write('New Y:', new_y)

        move_box(x, y, new_x, new_y)
        flood_fill(new_x, new_y, replace, two_d_arr[new_x, new_y])

    fig = plt.figure()
    img = plt.imshow(two_d_arr, cmap='rainbow', interpolation='none')
