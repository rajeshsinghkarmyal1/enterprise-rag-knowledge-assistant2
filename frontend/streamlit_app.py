import streamlit as st

st.set_page_config(
    page_title="Enterprise RAG Assistant",
    page_icon="🤖"
)

st.title("🤖 Enterprise RAG Knowledge Assistant")

question = st.text_input(
    "Ask a question about your documents"
)

if st.button("Submit"):

    st.success(
        "Response will be generated here."
    )

    st.write(
        "This is a sample response."
    )
