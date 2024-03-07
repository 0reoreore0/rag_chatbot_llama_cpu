import unittest
from typing import Dict, List
from chatllama.chat_history_manager import ChatHistoryManager

class ChatHistoryManagerTestCase(unittest.TestCase):

    def test_store_response(self):
        collection = ChatHistoryManager().store_response("this is a query","this is a response",2.34,"unit_test")
        self.assertTrue(any('query: this is a query' in turn for turn in collection))

    def test_fetch_session(self):
        result = ChatHistoryManager().fetch_session("fake_name")
        self.assertDictEqual(result, {})

x = ChatHistoryManagerTestCase()
x.test_fetch_session()
