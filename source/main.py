import streamlit as st
import streamlit.components.v1 as components
from graph import Graph

st.title("EU Legal documents visualised")
st.markdown("This application helps to **visualise EU documents** and the **relevant provisions cited   **.")

graph = Graph()
components.html(graph.defaultGraph, width=1000, height=550)

if st.button("Generate Visualisation"):
    graph.createGraph()
