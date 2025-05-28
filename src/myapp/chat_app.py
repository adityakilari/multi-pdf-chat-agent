import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from helpers.pdf_utils import get_pdf_text, get_text_chunks
from helpers.vector_utils import get_vector_store, load_vector_store
from helpers.rag_utils import get_conversational_chain

def user_input(user_question):
    db = load_vector_store()
    docs = db.similarity_search(user_question)
    chain = get_conversational_chain()
    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
    st.write("Reply: ", response["output_text"])

def main():
    st.set_page_config("Chat PDF")
    st.header("Ask for Requirements")
    user_question = st.text_input("Ask a Question from the PDF Files")
    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                chunks = get_text_chunks(raw_text)
                get_vector_store(chunks)
                st.success("Done")

if __name__ == "__main__":
    main()
