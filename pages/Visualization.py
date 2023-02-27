import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(
    page_title = "VISUALIZATION",
    page_icon = ":heartbeat:"
)

df = st.session_state.df


col1, col2 = st.columns(2)
type_anys = col1.selectbox('Select the type of Analysis', options = ['Uni-varient', 'Bi-varient', 'multi-varient'])

num_cols = df.select_dtypes(include = ['int', 'float']).columns.tolist()
cat_cols = df.select_dtypes(exclude = ['int', 'float']).columns.tolist()

if type_anys == 'Uni-varient' :
    col1, col2 = st.columns(2)
    x_axis_val = col1.selectbox('Select the X-axis', options = df.columns)

    if x_axis_val in num_cols:

        col1, col2 = st.columns(2)

        fig_1 = px.histogram(df, x = x_axis_val)
        col1.plotly_chart(fig_1, use_container_width = True)
        plot = px.box(df, x = x_axis_val)
        col2.plotly_chart(plot, use_container_width = True)

    else:
        col1, col2 = st.columns(2)

        fig_1 = px.pie(df, names = x_axis_val)
        col1.plotly_chart(fig_1, use_container_width = True)

elif type_anys == 'Bi-varient':
    col1, col2 = st.columns(2)
    x_axis_val = col1.selectbox('Select the X-axis', options = df.columns)
    y_axis_val = col2.selectbox('Select the Y-axis', options = df.columns)

    if x_axis_val in num_cols and y_axis_val in num_cols:
        plot = px.scatter(df, x = x_axis_val, y = y_axis_val)
        st.plotly_chart(plot, use_container_width =True)

    elif x_axis_val in cat_cols and y_axis_val in cat_cols:
        plot = px.histogram(df, x = x_axis_val, y = y_axis_val)
        st.plotly_chart(plot, use_container_width =True)

    else:
        plot = px.box(df, x = x_axis_val, y = y_axis_val)
        st.plotly_chart(plot, use_container_width =True)


else:
    col1, col2, col3 = st.columns(3)
    x_axis_val = col1.selectbox('Select the X-axis', options = df.columns)
    y_axis_val = col2.selectbox('Select the Y-axis', options = df.columns)
    color = col3.selectbox('Select the hue', options = cat_cols)

    plot = px.scatter(df, x = x_axis_val, y = y_axis_val, color = color)
    st.plotly_chart(plot, use_container_width = True)

    fig, ax = plt.subplots()
    plot = sns.heatmap(df.corr(), annot = True, ax = ax)
    st.write(fig)



