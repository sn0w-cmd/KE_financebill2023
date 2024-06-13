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
st.title("How did your MP Vote on the Finance Bill 2024?",)




with st.form("my_form"):
#    st.write("Inside the form")
   input_query = st.text_input("Enter the name of your constituency (or county for woman rep)")
   submitted = st.form_submit_button("Search")
   if submitted:
       input_query = input_query.upper()
       updated_df = df[df["Constituency"].str.contains(input_query)]
       st.dataframe(data=updated_df, use_container_width = True)
   


# # Upload image through Streamlit
# # input_query = st.text_input("Enter the name of your constituency")

# # uploaded_file = st.file_uploader("Choose an image...", type="jpg")
# normalized_counts = pd.DataFrame(df['Vote'].value_counts(ascending=False))

# # Plot bar chart

# st.bar_chart(normalized_counts, x=None, y='Vote')



st.subheader("Full records")
st.dataframe(data=df, use_container_width = True)


# # Upload image through Streamlit
# input_query = st.text_input("Enter the name of your constituency")
# # uploaded_file = st.file_uploader("Choose an image...", type="jpg")



# if input_query is not None:
#     # Display the uploaded image
#     input_query = input_query.capitalize()
#     # df[df['Constituency'] == input_query]
#     st.write(df[df['Constituency'] == input_query])


