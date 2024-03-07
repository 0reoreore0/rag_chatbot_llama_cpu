import unittest
from typing import Dict, List
from chatllama.pdf_vectorizer import PdfVectorizer

class PdfVectorizerTestCase(unittest.TestCase):

    def _get_pdf_vectorizer(self):
        pdf_vectorizer = PdfVectorizer(chunk_size=1000, chunk_overlap=200)
        return pdf_vectorizer

    def test_load_and_split_pdf(self):
        pdf_vectorizer = self._get_pdf_vectorizer()
        chunks = pdf_vectorizer.load_and_split_pdf()
        self.assertIsInstance(chunks, List)
        self.assertIsInstance(chunks[0].page_content, str)

    def test_embed_and_load_vector_db(self):
        pdf_vectorizer = self._get_pdf_vectorizer()
        db = pdf_vectorizer.embed_and_load_vector_db()
        self.assertIsInstance(db.get(), Dict)

x = PdfVectorizerTestCase()
x.test_embed_and_load_vector_db()
