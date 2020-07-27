import streamlit as st
import streamlit.components.v1 as components
from source.graph import Graph

from source.variables import *

graph = Graph()

st.title("EU Legal documents visualised")
st.markdown("This application helps to **visualise EU documents** and the **relevant provisions cited   **.")
option = st.selectbox('Select one piece of lex to visualise: ', ('', 'Example 1', 'Example 2', 'Example 3'))
if option == 'Example 1':
    graph.defaultGraph = example1
# if st.button("Generate Visualisation"):
#     graph.createGraph()
components.html(graph.defaultGraph, width=1000, height=550)
