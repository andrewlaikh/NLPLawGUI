"""This application experiments with the (grid) layout and some styling

Can we make a compact dashboard across several columns and with a dark theme?"""
import io
from typing import List, Optional

import markdown
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from plotly import express as px
from plotly.subplots import make_subplots
from source.graph import Graph
import streamlit.components.v1 as components
from source.layout import local_css

# matplotlib.use("TkAgg")
matplotlib.use("Agg")
COLOR = "black"
BACKGROUND_COLOR = "#fff"


def main():
    """Main function. Run this to run the app"""
    # st.sidebar.header("Settings")
    st.title("European Union Legislation Visualised")
    st.write("The following illustrations help to illustrate European Union Legislation and provisions cited in a document.")
    st.write("Select an option to visualise in the dropdown.")
    option = st.selectbox('', ('', 'Example 1', 'Example 2', 'Example 3'))
    graph = Graph()
    components.html(graph.defaultGraph, width=1200, height=500)
    local_css("style.css")
    st.markdown('**The text below shows relevant sections highlighted by the transformer models.**')
    t = "<div>Hello there my <span class='highlight blue'>name <span class='bold'>yo</span> </span> is <span class='highlight red'>Fanilo <span class='bold'>Name</span></span></div>"
    st.markdown(t, unsafe_allow_html=True)
    select_block_container_style()
    # add_resources_section()

    # My preliminary idea of an API for generating a grid
    # with Grid("1 1 1", color=COLOR, background_color=BACKGROUND_COLOR) as grid:
    #     grid.cell(
    #         class_="a",
    #         grid_column_start=2,
    #         grid_column_end=3,
    #         grid_row_start=1,
    #         grid_row_end=2,
    #     ).markdown("# This is A Markdown Cell")
    #     # Column start, column end, row start, row end
    #     grid.cell("b", 2, 3, 2, 3).text("The cell to the left is a dataframe")
    #     # grid.cell("b", 1, 4, 1, 4).visualisation_chart()
    #     grid.cell("c", 4, 4, 4,     4).visualisation_chart()
    #     # grid.cell("c", 3, 4, 2, 3).plotly_chart(get_plotly_fig())
    # grid.cell("d", 1, 2, 1, 3).dataframe(get_dataframe())
    # grid.cell("e", 3, 4, 1, 2).markdown(
    #     "Try changing the **block container style** in the sidebar!"
    # )
    # grid.cell("f", 1, 3, 3, 4).text(
    #     "The cell to the right is a matplotlib svg image"
    # )
    # grid.cell("g", 3, 4, 3, 4).pyplot(get_matplotlib_plt())

    # st.plotly_chart(get_plotly_subplots())


# def add_resources_section():
#     """Adds a resources section to the sidebar"""
#     st.sidebar.header("Add_resources_section")
#     st.sidebar.markdown(
#         """
# - [gridbyexample.com] (https://gridbyexample.com/examples/)
# """
#     )


class Cell:
    """A Cell can hold text, markdown, plots etc."""

    def __init__(
            self,
            class_: str = None,
            grid_column_start: Optional[int] = None,
            grid_column_end: Optional[int] = None,
            grid_row_start: Optional[int] = None,
            grid_row_end: Optional[int] = None,
    ):
        self.class_ = class_
        self.grid_column_start = grid_column_start
        self.grid_column_end = grid_column_end
        self.grid_row_start = grid_row_start
        self.grid_row_end = grid_row_end
        self.inner_html = ""

    def _to_style(self) -> str:
        return f"""
.{self.class_} {{
    grid-column-start: {self.grid_column_start};
    grid-column-end: {self.grid_column_end};
    grid-row-start: {self.grid_row_start};
    grid-row-end: {self.grid_row_end};
}}
"""

    def text(self, text: str = ""):
        self.inner_html = text

    def markdown(self, text):
        self.inner_html = markdown.markdown(text)

    def dataframe(self, dataframe: pd.DataFrame):
        self.inner_html = dataframe.to_html()

    def visualisation_chart(self):
        self.inner_html = markdown.markdown(defaultGraph)

    def markdown(self, text):
        self.inner_html = markdown.markdown(text)

    def pyplot(self, fig=None, **kwargs):
        string_io = io.StringIO()
        plt.savefig(string_io, format="svg", fig=(2, 2))
        svg = string_io.getvalue()[215:]
        plt.close(fig)
        self.inner_html = '<div height="200px">' + svg + "</div>"

    def _to_html(self):
        return f"""<div class="box {self.class_}">{self.inner_html}</div>"""


class Grid:
    """A (CSS) Grid"""

    def __init__(
            self,
            template_columns="1 1 1",
            gap="10px",
            background_color=COLOR,
            color=BACKGROUND_COLOR,
    ):
        self.template_columns = template_columns
        self.gap = gap
        self.background_color = background_color
        self.color = color
        self.cells: List[Cell] = []

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        st.markdown(self._get_grid_style(), unsafe_allow_html=True)
        st.markdown(self._get_cells_style(), unsafe_allow_html=True)
        st.markdown(self._get_cells_html(), unsafe_allow_html=True)

    def _get_grid_style(self):
        return f"""
<style>
    .wrapper {{
    display: grid;
    grid-template-columns: {self.template_columns};
    grid-gap: {self.gap};
    background-color: {self.background_color};
    color: {self.color};
    }}
    .box {{
    background-color: {self.color};
    color: {self.background_color};
    border-radius: 5px;
    padding: 20px;
    font-size: 150%;
    }}
    table {{
        color: {self.color}
    }}
</style>
"""

    def _get_cells_style(self):
        return (
                "<style>"
                + "\n".join([cell._to_style() for cell in self.cells])
                + "</style>"
        )

    def _get_cells_html(self):
        return (
                '<div class="wrapper">'
                + "\n".join([cell._to_html() for cell in self.cells])
                + "</div>"
        )

    def cell(
            self,
            class_: str = None,
            grid_column_start: Optional[int] = None,
            grid_column_end: Optional[int] = None,
            grid_row_start: Optional[int] = None,
            grid_row_end: Optional[int] = None,
    ):
        cell = Cell(
            class_=class_,
            grid_column_start=grid_column_start,
            grid_column_end=grid_column_end,
            grid_row_start=grid_row_start,
            grid_row_end=grid_row_end,
        )
        self.cells.append(cell)
        return cell


def select_block_container_style():
    """Add selection section for setting setting the max-width and padding
    of the main block container"""
    _set_block_container_style()
    # st.sidebar.header("Block Container Style")
    # max_width_100_percent = st.sidebar.checkbox("Max-width: 100%?", False)
    # if not max_width_100_percent:
    #     max_width = st.sidebar.slider("Select max-width in px", 100, 2000, 1200, 100)
    # else:
    #     max_width = 1200
    # dark_theme = st.sidebar.checkbox("Dark Theme?", False)
    # padding_top = st.sidebar.number_input("Select padding top in rem", 0, 200, 5, 1)
    # padding_right = st.sidebar.number_input("Select padding right in rem", 0, 200, 1, 1)
    # padding_left = st.sidebar.number_input("Select padding left in rem", 0, 200, 1, 1)
    # padding_bottom = st.sidebar.number_input(
    #     "Select padding bottom in rem", 0, 200, 10, 1
    # )
    # if dark_theme:
    #     global COLOR
    #     global BACKGROUND_COLOR
    #     BACKGROUND_COLOR = "rgb(17,17,17)"
    #     COLOR = "#fff"
    # _set_block_container_style(
    #     max_width,
    #     max_width_100_percent,
    #     padding_top,
    #     padding_right,
    #     padding_left,
    #     padding_bottom,
    # )


def _set_block_container_style(
        max_width: int = 1000,
        max_width_100_percent: bool = False,
        padding_top: int = 5,
        padding_right: int = 0,
        padding_left: int = 0,
        padding_bottom: int = 10,
):
    if max_width_100_percent:
        max_width_str = f"max-width: 100%;"
    else:
        max_width_str = f"max-width: {max_width}px;"
    st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        {max_width_str}
        padding-top: {padding_top}rem;
        padding-right: {padding_right}rem;
        padding-left: {padding_left}rem;
        padding-bottom: {padding_bottom}rem;
    }}
    .reportview-container .main {{
        color: {COLOR};
        background-color: {BACKGROUND_COLOR};
    }}
</style>
""",
        unsafe_allow_html=True,
    )


#
# @st.cache
# def get_dataframe() -> pd.DataFrame():
#     """Dummy DataFrame"""
#     data = [
#         {"quantity": 1, "price": 2},
#         {"quantity": 3, "price": 5},
#         {"quantity": 4, "price": 8},
#     ]
#     return pd.DataFrame(data)
#
#
# def get_plotly_fig():
#     """Dummy Plotly Plot"""
#     return px.line(data_frame=get_dataframe(), x="quantity", y="price")
#
#
# def get_matplotlib_plt():
#     get_dataframe().plot(kind="line", x="quantity", y="price", figsize=(5, 3))
#
#
# def get_plotly_subplots():
#     fig = make_subplots(
#         rows=2,
#         cols=2,
#         subplot_titles=("Plot 1", "Plot 2", "Plot 3", "Table 4"),
#         specs=[
#             [{"type": "scatter"}, {"type": "scatter"}],
#             [{"type": "scatter"}, {"type": "table"}],
#         ],
#     )
#
#     fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]), row=1, col=1)
#
#     fig.add_trace(go.Scatter(x=[20, 30, 40], y=[50, 60, 70]), row=1, col=2)
#
#     fig.add_trace(go.Scatter(x=[300, 400, 500], y=[600, 700, 800]), row=2, col=1)
#
#     fig.add_table(
#         header=dict(values=["A Scores", "B Scores"]),
#         cells=dict(values=[[100, 90, 80, 90], [95, 85, 75, 95]]),
#         row=2,
#         col=2,
#     )
#
#     if COLOR == "black":
#         template = "plotly"
#     else:
#         template = "plotly_dark"
#     fig.update_layout(
#         height=500,
#         width=700,
#         title_text="Plotly Multiple Subplots with Titles",
#         template=template,
#     )
#     return fig


main()
