import json
from langchain.chat_models import ChatOpenAI
from langchain.chains import create_tagging_chain
from pprint import pprint

file_path = "Machine Learning Projects\Project5\schema2.json"

message = '''Subject: Suggestion: Add Export to PDF Feature

Hi Development Team,

I love using your application, and I have a suggestion. Could you add an "Export to PDF" feature? It would make sharing documents so much easier.

I understand this is not urgent, but I think many users would appreciate it.

Thanks for considering my idea!'''


file = open(file_path)
data = json.load(file)
num_levels = len(data)-1
llm = ChatOpenAI(
    openai_api_key=data["openAI"]["openAIAPIkey"],
    model=data["openAI"]["modelName"],
    temperature=data["openAI"]["temperature"],
    max_tokens=data["openAI"]["maxTokens"]
)

schema = {
    "properties": {},
    "required": []
}

for i in range(1, num_levels+1):
    for j in range(len(data["level"+str(i)])):
        info = data["level"+str(i)][j]
        if i == 1:
            name = info["name"]
            schema["properties"][name] = {
                "type": info["type"],
                "enum": info["classesRequired"].split(','),
                "description": info["description"]
            }
            schema["required"].append(name)
            chain = create_tagging_chain(schema, llm)
            category = chain.run(message)
        else:
            classifier = info["classifierType"]
            type = info["if"]
            name = info["name"]
            if category[classifier] == type:
                schema["properties"][name] = {
                    "type": info["type"],
                    "enum": info["classesRequired"].split(','),
                    "description": info["description"]
                }
                schema["required"].append(name)
                chain = create_tagging_chain(schema, llm)
                category = chain.run(message)
    
pprint(category)


