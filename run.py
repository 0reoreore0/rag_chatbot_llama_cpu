from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from chatllama import ChatLlama

SESSION_NAME = "150_10"

chatllama = ChatLlama()
app = FastAPI()

@app.post('/chat')
async def get_response(query, chat_history=[]):
    return chatllama.chat(query, SESSION_NAME)

@app.get('/chat_history', response_class=PlainTextResponse)
async def get_session_history(session_name:str=SESSION_NAME):
    chat_history = chatllama.view_chat_history(session_name)
    return "\n\n".join(chat_history)
