### Setup
1. Activate a new virtual environment and navigate to `/rag_llama_chatbot_cpu`  
2. Run `pip install -e .`  

### Download data
1. Download `TheBloke/Llama-2-7B-Chat-GGUF` (https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF)
- Note 1: This repository requires Llama 2 models in `gguf` format  
- Note 2: You need to have a unique commercial license URL from Meta (https://llama.meta.com/llama-downloads) and have your model access request approved by the repo authors on Hugging Face as prerequisites.  
- Note 3: Create a folder named `model` and place the GGUF file there.  

2. Download the paper "Llama 2: Open Foundation and Fine-Tuned Chat Models" (https://arxiv.org/pdf/2307.09288.pdf)
- Note 1: Create a folder named `data` and place the PDF file there.  

### Running
1. Run `uvicorn run:app --host=0.0.0.0` in your terminal.
- If this is the first time you are splitting the PDF document into your current `chunk_size` and `chunk_overlap`, you will see logger messages indicating that the PDF is being split, vectorized, and stored into a database.  
- Once you see that `Uvicorn running on http://0.0.0.0:8000`, go to http://0.0.0.0:8000/docs and try out the displayed methods.    

**and/or**    

2. Run `python chatllama_ui.py` in your terminal.
- Again, if this is the first time you are splitting the PDF document into your current `chunk_size` and `chunk_overlap`, you will see logger messages indicating that the PDF is being split, vectorized, and stored into a database.  
- Once you see that it is `Running on local URL:  http://127.0.0.1:7860`, go to the URL in your browser and start chatting. On the left you can see a chatbot interface. On the right you can see a cumulative history of the current chat session that also includes latency per chatbot response.  

* *Note: `chatllama_ui` simply wraps the two methods in `run.py` - chat history database is consistent* *

### Examples (note: session name indicates chunk size and chunk overlap)
![chunk_size=50, chunk_overlap=5](/example_chats/50_5.png)
![chunk_size=150, chunk_overlap=10](/example_chats/150_10.png)
![chunk_size=500, chunk_overlap=50](/example_chats/500_50.png)
![chunk_size=1000, chunk_overlap=200](/example_chats/1000_200.png)
# rag_chatbot_llama_cpu
# rag_chatbot_llama_cpu
