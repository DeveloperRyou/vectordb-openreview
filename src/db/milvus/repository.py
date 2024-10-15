import util.text as text_util

def save_text(collection, paper_id: int, text: str):
    text_embedding = text_util.text_to_embedding(text)
    collection.insert([
        [paper_id],
        [text_embedding],
    ])
    collection.flush()
    print(f"[Milvus] {paper_id} saved")

def find_paper_id_by_text(collection, text: str):
    text_embedding = text_util.text_to_embedding(text)
    search_params = {"metric_type": "L2", "params": {"nprobe": 10}}

    result = collection.search(data=[text_embedding], anns_field="paper_embedding", param=search_params, limit=3)
    id_list = []
    for hits in result:
        for hit in hits:
            id_list.append(hit.id)
    return id_list
        
