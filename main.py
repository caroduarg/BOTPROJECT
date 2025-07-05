from fastapi import FastAPI
from pydantic import BaseModel
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

model = init_chat_model('command-r-plus', model_provider='cohere')

messages = [
    SystemMessage(content="Eres un experto en la aviación y conoces todo lo relacionado al alfabeto fonético internacional (AFI). Responde a las preguntas de los usuarios de manera clara y concisa.")
]

app = FastAPI()

class bot(BaseModel):
    query: str

@app.post("/bot/")
async def botproject(q: bot):
    question=q.query
    messages.append(HumanMessage(question))
    response = model.invoke(messages) 
    messages.append(response)
    return messages[-1].content