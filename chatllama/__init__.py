from chatllama.pdf_vectorizer import PdfVectorizer
from chatllama.llama_loader import LlamaLoader
from chatllama.llama_agent import LlamaAgent
from chatllama.chat_history_manager import ChatHistoryManager

class ChatLlama():
    """
    Loads LLM & Chain only once, loads (or creates if doesn't exist already) vectorized PDF database only once before running chat agent.
    The chat feature returns a response while updating that chat session's chat history.
    The chat history viewing feature returns full chat history Chroma DB containing responses, queries, and latencies as documents.
    """
    def __init__(self):
        self.chain = LlamaLoader().chain
        self.db = PdfVectorizer(chunk_size=150, chunk_overlap=10).embed_and_load_vector_db()
        self.agent = LlamaAgent()
        self.chat_history_manager = ChatHistoryManager()

    def chat(self, query, session_name):
        response, latency = self.agent.run_agent(self.chain, query, self.db)
        chat_hist = self.chat_history_manager.store_response(query, response, latency, session_name)
        return response

    def view_chat_history(self, session_name):
        return self.chat_history_manager.fetch_session(session_name)
