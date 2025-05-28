import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.appconfig import OLLAMA_MODEL
from langchain_community.chat_models import ChatOllama
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate


def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details. 
    If the answer is not in the provided context, just say "answer is not available in the context".
    
    Context:\n {context}?\n
    Question: \n{question}\n
    Answer:
    """
    model = ChatOllama(model=OLLAMA_MODEL, temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    return load_qa_chain(model, chain_type="stuff", prompt=prompt)
