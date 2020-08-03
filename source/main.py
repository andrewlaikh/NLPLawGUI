import re
import streamlit as st
import streamlit.components.v1 as components
from source.graph import Graph
from source.layout import local_css
from source.layout import set_block_container_style

graph = Graph()

st.title("EU Legal documents visualised")
st.markdown("This application helps to **visualise EU documents** and the **relevant provisions cited   **.")
option = st.selectbox('Select one piece of lex to visualise: ', ('', 'Example 1', 'Example 2', 'Example 3'))
if option:
    num = re.search(r"\d", option).group(0)
    graph.createGraph(num)
    graph.defaultGraphText = graph.returnGraphText(num)
components.html(graph.defaultGraph, width=1000, height=550)
set_block_container_style()
st.markdown('**The text below shows relevant sections highlighted by a BERT model.**')
local_css("style.css")
st.markdown(r'<div>' + graph.defaultGraphText + r'</div>', unsafe_allow_html=True)