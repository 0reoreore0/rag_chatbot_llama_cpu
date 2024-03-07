import unittest
from unittest import mock
from chatllama.llama_agent import LlamaAgent

class LlamaAgentTestCase(unittest.TestCase):

    def _get_agent(self):
        agent = LlamaAgent()
        query = "what is llama 2?"
        return agent, query

    @mock.patch("chromadb.api.models.Collection.Collection")
    @mock.patch("langchain.chains.LLMChain")
    def test_run_agent(self, mock_db, mock_chain):
        agent, query = self._get_agent()
        db = mock_db.return_value
        chain = mock_chain.return_value
        agent.run_agent(chain, query, db)
        self.assertTrue(db.query.called)
        self.assertTrue(chain.invoke.called)

x = LlamaAgentTestCase()
x.test_run_agent()
