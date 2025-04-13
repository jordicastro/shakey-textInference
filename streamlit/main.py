import streamlit as st

pages = {
    "home": [
        st.Page("home.py", title="Home"),
        st.Page("evalMetrics.py", title="Eval Metrics"),
    ]
}

pg = st.navigation(pages, position="hidden")
pg.run()

