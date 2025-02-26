import streamlit as st
from propelauth import auth

user = auth.get_user()
if user is None:
    st.error("Unauthorized")
    st.stop()

with st.sidebar:
    st.link_button("Account", auth.get_account_url(), use_container_width=True)
    if st.button("Logout", use_container_width=True):
        auth.logout()
        st.markdown(
            """
        <meta http-equiv="refresh" content="0; URL='/api/auth/logout'" /> 
            """,
            unsafe_allow_html=True,
        )

pages = {
    "Navigation Menu": [
        st.Page("invoice_extractor.py", title="Invoice Extractor"),
        st.Page("invoice_downloads.py", title="Download Extracted Invoices"),
    ]
}

pg = st.navigation(pages)
pg.run()
