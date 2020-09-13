import streamlit as st
from pyvis.network import Network
import os
import networkx as nx
import itertools


# Can try to fix for session specific ID later, but leave it for now.
@st.cache(allow_output_mutation=True)
class Graph:
    def __init__(self):
        self.defaultGraph = self.returnGraph(2)
        self.defaultGraphText = self.returnGraphText(2)

    def returnGraph(self, num):
        fileName = 'example' + str(num) + r'.html'
        with open(fileName, 'r') as file:
            text = file.read()
            text = text.replace('border: 1px', 'border: 0px')
        return text

    def createGraph(self, num):
        self.defaultGraph = self.returnGraph(num)

    def returnGraphText(self, num):
        fileName = 'html' + str(num) + r'Text.html'
        with open(fileName, 'r', errors='ignore') as file:
            text = file.read()
            text = text.replace('border: 1px', 'border: 0px')
        text = text.lower()
        for line in text.splitlines():
            line = line.strip()
        with open("copy.txt", "w") as file:
            file.write(text)
        return text
