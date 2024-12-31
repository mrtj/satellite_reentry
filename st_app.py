import streamlit as st
from io import StringIO
from satellite_reentry import load_satevo
import plotly.express as px  # type: ignore

st.set_page_config("SatEvo log visualizer", page_icon="☄️")

uploaded_file = st.file_uploader("Upload SatEvo log file")
if uploaded_file is not None:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    df = load_satevo(stringio)
    plot = px.line(df)
    plot.update_layout(
        yaxis_title="Altitude [km]",
    )
    st.plotly_chart(plot)
    st.markdown(
        f"Last data point:\n\n"
        f"- date: {df.index[-1]}\n"
        f"- apogee: {df.iloc[-1]['apogee']}\n"
        f"- perigee: {df.iloc[-1]['perigee']}\n"
)