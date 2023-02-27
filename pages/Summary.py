import streamlit as st
import io



st.set_page_config(
    page_title =  "'SUMMARY",
    page_icon = ":heartbeat:"
)

df = st.session_state.df
df2 = st.session_state.df
buffer = io.StringIO()
buffer2 = io.StringIO()
st.subheader("Basic info about data")
df.info(buf = buffer)
s = buffer.getvalue()
st.code(s, language = None)

st.subheader('Basic description of data')
st.table(df.describe().T)

st.subheader('NO. of duplicate and null rows dropped')
st.code(df.shape[0] - df.drop_duplicates().dropna().shape[0], language = None)

df2 = df2.drop_duplicates().dropna()

df2.info(buf = buffer2)
d = buffer2.getvalue()
st.code(d, language = None)

