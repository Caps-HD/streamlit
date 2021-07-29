import streamlit as st

from tool.DataTool import DataTool

add_select_box = st.sidebar.selectbox(
    "请选择模块?",
    ("数据处理工具", "其他")
)

if add_select_box == '数据处理工具':
    DataTool(st).data_tool()

