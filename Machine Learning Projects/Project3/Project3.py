import openai
import pandas as pd
import numpy as np
from openai.embeddings_utils import cosine_similarity
from openai.embeddings_utils import get_embedding
from IPython.display import display
 
openai.api_key = '' 

HAQ_df = pd.read_csv(r"Machine Learning Projects\Project3\HAQData.csv", encoding='unicode_escape')

HAQ_df['embedding'] = HAQ_df['HA Question'].apply(lambda x: get_embedding(x, engine='text-embedding-ada-002'))
HAQ_df.to_csv('HAQ-embeddings.csv')

HAQ_search = input("Search HAQ for a sentence/word:")

HAQ_search_vector = get_embedding(HAQ_search, engine="text-embedding-ada-002")
HAQ_search_vector

HAQ_df['embedding'] = HAQ_df['embedding'].apply(np.array)
HAQ_df['similarities'] = HAQ_df['embedding'].apply(lambda x: cosine_similarity(x, HAQ_search_vector))

sorted_HAQ_df = HAQ_df.sort_values("similarities", ascending=False)
display(sorted_HAQ_df)

