import streamlit as st
import pandas


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("David Boadu")
    content = """
    I am a seasoned Python and DevOps engineer with a track record of collaborating with diverse organizations.
    My expertise includes constructing robust CI/CD pipelines, addressing networking challenges, 
    architecting efficient cloud infrastructures, and enhancing the performance of Python applications.
    """
    st.info(content)

st.write("Below you can find some of the apps i have built in Python. Feel free to contact me!")

col3,empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep=";")


with col3:

    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")