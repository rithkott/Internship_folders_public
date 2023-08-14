from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import pprint

leave_arr = ["Leave Policy", "Machine Learning Projects\Project1\leave_policy_document.txt"]
global_reimbursement_arr = ["Global Reimbursement Policy", "Machine Learning Projects\Global reimbursement Policy.txt"]
moonlighting_arr = ["Moonlighting Policy", "Machine Learning Projects\Moonlighting Policy.txt"]
allowance_arr = ["Shift Allowance Policy", "Machine Learning Projects\Shift Allowance Policy.txt"]
travel_arr = ["Travel and Accomodation Policy", "Machine Learning Projects\Travel and Accomodation Policy.txt"]

full_arr = [leave_arr, global_reimbursement_arr, moonlighting_arr, allowance_arr, travel_arr]

model = SentenceTransformer('intfloat/e5-large-v2')

search = "query: Maternity Leave"

closest_text = None
closest_similarity = 0
for i in full_arr:
    input_text = [search, "query: " + i[0]]
    embeddings = model.encode(input_text, normalize_embeddings=True)
    similarity = cosine_similarity(embeddings)[1][0]
    if similarity > closest_similarity:
        closest_similarity = similarity
        closest_text = i

print(closest_text[0])

file = open(closest_text[1], 'r', encoding='unicode_escape')
    
lines = file.readlines()

blocks = []
current_block = ""

for line in lines:
    stripped_line = line.strip()
    
    if stripped_line: 
        current_block += '  '
        current_block += line

    else:
        if current_block:  # If the block is not empty
            blocks.append(current_block)
            current_block = ""

# Append the last block if it's not empty
if current_block:
    blocks.append(current_block)
        
closest_similarity = 0

for i in blocks:
    input_text = [search, "query: " + i]
    embeddings = model.encode(input_text, normalize_embeddings=True)
    similarity = cosine_similarity(embeddings)[1][0]
    if similarity > closest_similarity:
        closest_similarity = similarity
        closest_block = i
    
print(closest_block)

