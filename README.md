# About

- A chat agent that will read multiple pdf's and provide valid text output 
- RAG design pattern with Ollama and langchain frameworks uses Mistral model and chroma db

# To create and activate virtual env

- conda create -p ./venv python=3.12; (take the appropriate python version, venv -> name can be anything)
- conda activate venv/ 

# To install all the required packages to virtual env

- pip install -r requirements.txt 

# Docker image for ollama

- compose.yml file is attached. or

-docker pull ollama/ollama:latest
-docker run -d -p 11434:11434 --name ModelOllama ollama/ollama
-docker list (to see list of models exist)
-docker pull <any_model_you_need>