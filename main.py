import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Amirali Shadrou")
    content = """
    Hi i am amirali. Im a python programmer.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in python. Feel free to contact me!
"""

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
