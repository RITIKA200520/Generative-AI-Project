from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name ="sentence-transformers/all-MiniLM-L6-v2"
)

texts = [
    "hello sweet",
    "my name is cute",
    "the world is beautiful"
]


vector =embedding.embed_documents(texts)

print(vector)