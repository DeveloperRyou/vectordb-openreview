from sentence_transformers import SentenceTransformer

def text_to_embedding(text):
    transformer = SentenceTransformer('paraphrase-mpnet-base-v2')
    embedding = transformer.encode(text, show_progress_bar=False)
    return embedding