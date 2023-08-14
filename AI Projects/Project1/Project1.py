#using e5_base_v2 encoder
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('intfloat/e5-large-v2')
input_text = ["Can I wear jeans to the office?", "Dress Code Policy"]
embeddings = model.encode(input_text, normalize_embeddings=True)

print(cosine_similarity(embeddings)[1][0])





