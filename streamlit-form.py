import streamlit as st
import pandas as pd
from datetime import datetime, time

# 设置页面标题
st.title("Streamlit 完整表单示例")
st.markdown("这个表单包含了 Streamlit 支持的所有组件类型")

# 创建表单
with st.form("my_form"):
    st.subheader("1. 文本输入组件")
    text_input = st.text_input("普通文本输入")
    text_input1 = st.text_input("普通文本输入1")
    text_area = st.text_area("多行文本输入", height=100)
    number_input = st.number_input("数字输入", min_value=0, max_value=100, value=50, step=1)

    st.subheader("2. 选择组件")
    selectbox = st.selectbox("下拉选择框", options=["选项1", "选项2", "选项3", "选项4"])
    multiselect = st.multiselect("多选框", options=["选项A", "选项B", "选项C", "选项D"], default=["选项A"])
    radio = st.radio("单选按钮", options=["选择1", "选择2", "选择3"])
    checkbox = st.checkbox("复选框")

    st.subheader("3. 日期时间组件")
    date_input = st.date_input("日期选择", value=datetime.now())
    time_input = st.time_input("时间选择", value=time(12, 0))
    date_range = st.date_input("日期范围选择", value=[datetime(2024, 1, 1), datetime(2024, 1, 31)])

    st.subheader("4. 文件上传组件")
    file_uploader = st.file_uploader("文件上传", type=["csv", "txt", "xlsx"])

    st.subheader("5. 媒体组件")
    # 摄像头组件
    camera_input = st.camera_input("拍照")

    st.subheader("6. 滑块组件")
    slider = st.slider("普通滑块", min_value=0, max_value=100, value=50)
    range_slider = st.slider("范围滑块", min_value=0, max_value=100, value=(25, 75))
    select_slider = st.select_slider("选择滑块", options=["非常低", "低", "中", "高", "非常高"], value="中")

    st.subheader("7. 颜色选择器")
    color_picker = st.color_picker("颜色选择", value="#FF0000")

    st.subheader("8. 数据展示组件（用于预览）")
    # 创建一个简单的DataFrame用于展示
    df = pd.DataFrame({
        "姓名": ["张三", "李四", "王五"],
        "年龄": [25, 30, 35],
        "城市": ["北京", "上海", "广州"]
    })
    st.dataframe(df)

    # 表单提交按钮
    submitted = st.form_submit_button("提交表单")

    # 表单提交后的处理
    if submitted:
        st.success("表单提交成功！")
        st.subheader("表单数据预览：")

        # 显示文本输入
        st.write("普通文本输入:", text_input)
        st.write("普通文本输入1:",text_input1)
        st.write("多行文本输入:", text_area)
        st.write("数字输入:", number_input)

        # 显示选择组件
        st.write("下拉选择框:", selectbox)
        st.write("多选框:", multiselect)
        st.write("单选按钮:", radio)
        st.write("复选框:", checkbox)

        # 显示日期时间组件
        st.write("日期选择:", date_input)
        st.write("时间选择:", time_input)
        st.write("日期范围选择:", date_range)

        # 显示文件上传组件（如果有上传文件）
        if file_uploader is not None:
            st.write("上传文件名:", file_uploader.name)
            # 如果是CSV文件，可以预览内容
            if file_uploader.type == "text/csv":
                df_uploaded = pd.read_csv(file_uploader)
                st.dataframe(df_uploaded.head())

        # 显示摄像头组件（如果有拍照）
        if camera_input is not None:
            st.image(camera_input, caption="拍摄的照片", width=300)

        # 显示滑块组件
        st.write("普通滑块:", slider)
        st.write("范围滑块:", range_slider)
        st.write("选择滑块:", select_slider)

        # 显示颜色选择器
        st.write("颜色选择:", color_picker)

        st.info("所有组件的数据都已成功收集！")

# 侧边栏示例
with st.sidebar:
    st.subheader("侧边栏组件")
    sidebar_selectbox = st.selectbox("侧边栏下拉框", options=["选项1", "选项2", "选项3"])
    sidebar_slider = st.slider("侧边栏滑块", min_value=0, max_value=100, value=30)
    sidebar_button = st.button("侧边栏按钮")

    if sidebar_button:
        st.write("侧边栏按钮被点击！")