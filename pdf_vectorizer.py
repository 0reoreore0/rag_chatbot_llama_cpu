import os
from chatllama.constants import DATA_FOLDER_PATH, PDF_FILENAME, VECTOR_DB_FOLDER_PATH
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
import chromadb
from loguru import logger

logger.level("PdfVectorizer", no=20, color="<fg 0,255,0>", icon="🧠")

class PdfVectorizer():
    """
    A class for loading vectorized PDF Chroma database if it already exists. If not, split PDF, vectorize, then create a new database.
    """
    def __init__(self, chunk_size:int, chunk_overlap:int):
        self.pdf_file = os.path.join(DATA_FOLDER_PATH, PDF_FILENAME)
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def load_and_split_pdf(self):
        logger.log("PdfVectorizer", f"loading and splitting pdf, chunk size {self.chunk_size}, chunk overlap {self.chunk_overlap}...")
        loader = PyPDFLoader(self.pdf_file)
        pdf_splitter = RecursiveCharacterTextSplitter(
                                length_function=len,
                                is_separator_regex=False,
                                chunk_size=self.chunk_size,
                                chunk_overlap=self.chunk_overlap
                        )
        chunks = loader.load_and_split(pdf_splitter)
        return chunks

    def embed_and_load_vector_db(self):
        client = chromadb.PersistentClient(path=VECTOR_DB_FOLDER_PATH)
        collection_exists=False
        logger.log("PdfVectorizer", f"checking if vectorized pdf database already exists...")
        while collection_exists!=True:
            try:
                collection = client.get_collection(name=f"pdf_{self.chunk_size}_{self.chunk_overlap}")
                collection_exists=True
                logger.log("PdfVectorizer", f"vectorized pdf database already exists")
            except Exception as e:
                logger.log("PdfVectorizer", f"vectorized pdf database doesn't exist")
                collection = client.create_collection(name=f"pdf_{self.chunk_size}_{self.chunk_overlap}")
                chunks = self.load_and_split_pdf()
                documents = [doc.page_content for doc in chunks]
                metadatas = [doc.metadata for doc in chunks]
                ids = [str(i) for i in range(len(chunks))]
                logger.log("PdfVectorizer", f"vectorizing data and adding to chromadb collection...")
                collection.add(documents=documents, metadatas=metadatas, ids=ids)
        logger.log("PdfVectorizer", f"successfully loaded pdf vector db")
        return collection
