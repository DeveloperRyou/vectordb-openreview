from pymilvus import CollectionSchema, FieldSchema, DataType, Collection, connections, db

def create_milvus_db():
    connections.connect(alias="default", host="localhost", port="19530")
    try:
        db.create_database("papers_db")
    except:
        pass
    db.using_database("papers_db")
    collection = None
    try:
        collection = get_collection()
        collection.load()
    except:
        collection = create_collection()
        create_index_collection(collection)
        collection.load()
    print(f"[Milvus] Collection loaded: {collection.name}")
    print(f"[Milvus] Collection schema: {collection.schema}")
    print(f"[Milvus] Collection data size: {collection.num_entities}")
    return collection

def create_collection():
    field_id = FieldSchema(name="paper_id", dtype=DataType.VARCHAR, max_length=256, is_primary=True)
    field_paper = FieldSchema(name="paper_embedding", dtype=DataType.FLOAT_VECTOR, dim=768)

    schema = CollectionSchema(fields=[field_id, field_paper], description="vector db for papers")

    # Create a collection
    collection = Collection(name="papers_collection", schema=schema)
    return collection

def create_index_collection(collection):
    index_params = {"index_type": "IVF_FLAT", "params": {"nlist": 128}, "metric_type": "L2"}
    collection.create_index(field_name="paper_embedding", index_params=index_params)

def get_collection():
    return Collection(name="papers_collection")

def drop_collection():
    try:
        collection = get_collection()
        collection.drop()
        print(f"[Milvus] Collection dropped")
    except:
        pass
