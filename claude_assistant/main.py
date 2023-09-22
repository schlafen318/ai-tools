from flask import Flask, jsonify, request
from dotenv import load_dotenv
from langchain.chat_models import ChatAnthropic
from langchain.chains import ConversationChain
from langchain.agents import Tool
from langchain.agents import AgentType
from langchain.utilities import SerpAPIWrapper
from langchain.agents import initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain.prompts.chat import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

load_dotenv()

load_dotenv()

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.run()
