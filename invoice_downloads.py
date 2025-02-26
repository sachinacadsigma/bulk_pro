import streamlit as st
import os
from propelauth import auth

user = auth.get_user()
if user is None:
    st.error("Unauthorized")
    st.stop()


st.header("My Invoices")

excel_files_dir = st.session_state["user_dir_path"]


@st.fragment
def download_file(book_path, file_name):
    with open(book_path, "rb") as f:
        st.download_button(
            label=f"Download {file_name}",
            data=f,
            file_name=file_name,
            mime="application/vnd.ms-excel",
        )


file_list = os.listdir(excel_files_dir)
if len(file_list) == 0:
    st.info("No invoices found, upload some invoices to get started!")
else:
    for file_name in os.listdir(excel_files_dir):
        book_path = os.path.join(excel_files_dir, file_name)
        download_file(book_path, file_name)
