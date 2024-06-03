import streamlit as st
from functions import get_and_write_todos

todos_complete = get_and_write_todos(filepath='pages/todo_done.txt')

for index, todo in enumerate(todos_complete):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        get_and_write_todos(remove_item=todo, filepath='pages/todo_done.txt')
        del todos_complete[index]
        del st.session_state[todo]
        st.rerun()
