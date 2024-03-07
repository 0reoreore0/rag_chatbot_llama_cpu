import os
from loguru import logger
from pathlib import Path
from chatllama.constants import MODEL_FOLDER_PATH, LLM_FILENAME
from langchain_community.llms import LlamaCpp
from langchain.chains import LLMChain
from langchain import hub

logger.level("LlamaLoader", no=20, color="<fg 0,255,0>")
class LlamaLoader():
    """
    A simple loader class for loading local Llama LLM and a Chain.
    """
    def __init__(
        self,
        model_path:str=os.path.join(MODEL_FOLDER_PATH, LLM_FILENAME),
        verbose:bool=True
        ):
        logger.log("LlamaLoader", f"loading {Path(LLM_FILENAME).stem}...")
        self.llm = LlamaCpp(model_path=model_path, n_ctx=2048, verbose=verbose)
        rag_prompt = hub.pull("rlm/rag-prompt-llama")
        logger.log("LlamaLoader", f"setting up llm chain for chatting...")
        self.chain = LLMChain(llm=self.llm, prompt=rag_prompt)
