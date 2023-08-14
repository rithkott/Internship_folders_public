from langchain.chat_models import ChatOpenAI
from langchain.chains import create_tagging_chain
import os

os.environ["OPENAI_API_KEY"] = ''
llm = ChatOpenAI(temperature=0, model='gpt-3.5-turbo')

schema = {
    "properties": {
        "urgency": {
        "type": "string",
        "enum": ["urgent", "not urgent"],
        'description': "Mark text as urgent if there is any text conveying the matter is time sensitive and must be resolved quickly"
        },
        "language": {
        "type": "string", 
        "enum": ["english", "spanish", "french"]  
        },
    },
    "required": ['urgency', 'language']
}

chain = create_tagging_chain(schema, llm)
results = chain.run("I hope you are doing well. I am reaching out to request some information regarding [specific topic or project]. There's no immediate urgency, but I would appreciate your assistance at your earliest convenience.")

print(results)