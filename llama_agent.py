import time
from loguru import logger

logger.level("LlamaAgent", no=20, color="<fg 0,255,0>", icon="🧠")
class LlamaAgent():
    """
    Agent class for querying db, then passing the query and the fetched search results through a Chain to generate LLM response.
    """
    def run_agent(self, chain, query:str, db):
        latency_start = time.time()
        logger.log("LlamaAgent", f"querying vector database...")
        docs = db.query(query_texts="Give me some facts about Llama2", n_results=3)
        docs = docs["documents"][0]
        logger.log("LlamaAgent", f"generating response...")
        response = chain.invoke({"context":docs, "question":query})
        response = response['text']
        latency_end = time.time()
        logger.log("LlamaAgent", f"\nuser query: {query} \nchatbot response: {response} \ntime taken: {latency_end-latency_start} seconds")
        return response, round(latency_end-latency_start, 2)
