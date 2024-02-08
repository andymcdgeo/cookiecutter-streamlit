import streamlit as st


if "{{ cookiecutter.include_src_directory }}" == 'y':
    from src.components import sidebar
    sidebar.show_sidebar()

st.title('{{ cookiecutter.project_slug }}')
st.write('{{ cookiecutter.project_description }}')