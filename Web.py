import streamlit as st
import functions

# Hide the Streamlit menu and "Made with Streamlit" watermark
st.set_page_config(
    page_icon=None,
    layout='centered',  # Can be "wide" or "centered".
    initial_sidebar_state='auto',  # Can be "auto", "expanded", "collapsed".
    menu_items={
        'Get Help': None,
        'Report a Bug': None,
        'About': None,
    }
)
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("My Todos App")
st.subheader("Increase your productivity.")

st.text_input(label="Enter a todo", placeholder="Add a new todo",
              on_change=add_todo, key='new_todo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

        st.session_state
