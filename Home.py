import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout="wide")

def add_todo():
    todo = st.session_state["new_todo"]+'\n'
    todos.append(todo)
    functions.write_todos(todos)

st.title('Todo アプリ')
st.subheader('パイソンで作成しました。')

st.write('<b>作：安田忠邦　<b>2022年12月クリマス</b>', unsafe_allow_html=True)

st.text_input(label="新しいtodo", placeholder="新しい項目を追加してください", on_change=add_todo, key="new_todo")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

