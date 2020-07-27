import streamlit as st
from pyvis.network import Network
from source.variables import *
import os


# Can try to fix for session specific ID later, but leave it for now.
@st.cache(allow_output_mutation=True)
class Graph:
    def __init__(self):
        self.defaultGraph = example1

    def updateVariable(self):
        with open('output.html', 'r') as file:
            text = file.read()
            text = text.replace('border: 1px', 'border: 0px')
            self.defaultGraph = text

    def createGraph(self):
        net = Network("500px", "950px")
        self.counter = self.counter + 1
        net.add_node(self.counter, label="Node " + str(self.counter))
        net.save_graph("output.html")
        self.updateVariable()
        os.remove("output.html")
