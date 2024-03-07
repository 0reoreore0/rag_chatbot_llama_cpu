import os
from chatllama.constants import DATA_FOLDER_PATH, PDF_FILENAME, VECTOR_DB_FOLDER_PATH
import chromadb
from loguru import logger

logger.level("ChatHistoryManager", no=20, color="<fg 0,255,0>", icon="🧠")
class ChatHistoryManager():
    """
    A class for storing chat history to Chroma database, and for fetching requested chat history by session name.
    """
    def __init__(self):
        self.client = chromadb.PersistentClient(path=VECTOR_DB_FOLDER_PATH)

    def store_response(self, query, response, latency, session_name):
        collection = self.client.get_or_create_collection(name=session_name)
        logger.log("ChatHistoryManager", f"updating chat history...")
        collection.add(documents=[f"\nquery: {query} \nresponse: {response}\nlatency: {latency} seconds"], ids=[str(collection.count()+1)])
        return collection.get()['documents']

    def fetch_session(self, session_name):
        logger.log("ChatHistoryManager", f"fetching chat history for chat session: '{session_name}'...")
        try:
            result = self.client.get_collection(name=session_name).get()['documents']
        except Exception as e:
            result = {}
        return result
