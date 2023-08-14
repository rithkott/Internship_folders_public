import openai
import pandas as pd
import numpy as np
from openai.embeddings_utils import cosine_similarity
from openai.embeddings_utils import get_embedding
from IPython.display import display
 
openai.api_key = '' 

HAQ_df = pd.read_csv(r"Machine Learning Projects\Project3\HAQData (1).csv", encoding='unicode_escape')

HAQ_df['embedding'] = HAQ_df['HA Question'].apply(lambda x: get_embedding(x, engine='text-embedding-ada-002'))
HAQ_df.to_csv('HAQ-embeddings.csv')

question = input("Enter your question: ")

HAQ_search_vector = get_embedding(question, engine="text-embedding-ada-002")
HAQ_search_vector

HAQ_df['embedding'] = HAQ_df['embedding'].apply(np.array)
HAQ_df['similarities'] = HAQ_df['embedding'].apply(lambda x: cosine_similarity(x, HAQ_search_vector))

sorted_HAQ_df = HAQ_df.sort_values("similarities", ascending=False)
display(sorted_HAQ_df)

knowledge = sorted_HAQ_df.iloc[0, 0] + '\n' + sorted_HAQ_df.iloc[0, 1]

response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=f'''Can you answer the below question using only the knowledge i provide. If there is not enough information present in the knowledge given below to answer say you cannot answer.
  
  Question: {question}

  Knowledge: {knowledge}
  
  Answer:
  ''',
  temperature=0.5,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0  
)

print(response["choices"][0]["text"])
