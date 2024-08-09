import streamlit as st
import pandas as pd

st.title("CSV Reading App")
uploaded_file = st.file_uploader("Click to upload CSV file", type="csv")

if uploaded_file is not None:
    st.success("File was uploaded...")
    data_frame = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(data_frame.head())

    st.subheader("Summary Table")
    st.write(data_frame.describe())

    st.subheader("Data Filtering")
    columns = data_frame.columns.tolist()
    selected_column = st.selectbox("Choose a column for a filtering", columns)
    column_unique_values = data_frame[selected_column].unique()
    selected_value = st.selectbox("Select value", column_unique_values)

    st.subheader("Filtered DataFrame")
    filtered_data_frame = data_frame[data_frame[selected_column] == selected_value]
    st.write(filtered_data_frame)

    st.subheader("Chart Data")
    x_column = st.selectbox("Choose a column for x-axis", columns)
    y_column = st.selectbox("Choose a column for y-axis", columns)

    if st.button("Generate Chart"):
        st.line_chart(filtered_data_frame.set_index(x_column)[y_column])


else:
    st.error("No file chosen...")
