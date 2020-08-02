import streamlit as st
from pyvis.network import Network
import os
import networkx as nx
import itertools

# Can try to fix for session specific ID later, but leave it for now.
@st.cache(allow_output_mutation=True)
class Graph:
    def __init__(self):
        self.defaultGraph = self.returnGraph(1)

    def returnGraph(self, num):
        fileName = 'example' + str(num) + r'.html'
        with open(fileName, 'r') as file:
            text = file.read()
            text = text.replace('border: 1px', 'border: 0px')
        return text

    def createGraph(self, num):
        self.defaultGraph = self.returnGraph(num)
        # net = Network("500px", "950px")
        # self.counter = self.counter + 1
        # net.add_node(self.counter, label="Node " + str(self.counter))
        # net.save_graph("output.html")
        # self.updateVariable()
        # os.remove("output.html")

    def returnGraphText(self, num):
        fileName = 'example' + str(num) + r'text.html'
        with open(fileName, 'r') as file:
            text = file.read()
            text = text.replace('border: 1px', 'border: 0px')
        return text
