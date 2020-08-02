import streamlit as st


def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


def set_block_container_style(
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
        color: {"black"};
        background-color: {"#fff"};
    }}
</style>
""",
        unsafe_allow_html=True,
    )
