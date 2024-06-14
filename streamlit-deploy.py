import streamlit as st
import pandas as pd

# Load your DataFrame
df = pd.read_csv('financebillvotes.csv')



# Streamlit app
st.set_page_config(
    page_title="Finance Bill Votes",
    page_icon="🗳️",
    layout="centered",
    initial_sidebar_state="expanded",
)


st.sidebar.title("About")
st.sidebar.info(
    
    "IS ABSENCE = YES?"
)
st.title("How did your MP Vote on the Finance Bill 2024?")



input_query = st.text_input("Enter the name of your constituency (or county for woman rep)")
submitted = st.button("Search")
if submitted:
    input_query = input_query.upper()
    updated_df = df[df["Constituency"].str.contains(input_query)]

    st.dataframe(data=updated_df, column_order=("Other Names", "Constituency", "Vote"), hide_index=True)



st.subheader("Full records")
st.dataframe(data=df)
