import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("The list of tasks:")
st.write("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo.capitalize())

st.text_input(label="Enter a todo:", placeholder="Add new todo...")


