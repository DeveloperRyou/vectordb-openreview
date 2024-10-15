from fastapi import FastAPI, Query
import db.milvus.model as milvus_model
import db.milvus.repository as milvus_repository
import db.mysql.model as mysql_model
import db.mysql.repository as mysql_repository

#milvus_model.drop_collection()
milvus_collection = milvus_model.create_milvus_db()
mysql_db = mysql_model.create_mysql_db()
app = FastAPI()

@app.get("/health")
def read_root():
    return {"health": "OK"}

@app.get("/search")
def read_item(text: str = Query(..., title="Text to search", description="Text to search in the database")):
    id_list = milvus_repository.find_paper_id_by_text(milvus_collection, text)
    print(id_list)
    result = []
    for id in id_list:
        forum = mysql_repository.find_forum_by_id(mysql_db, id)
        review = mysql_repository.find_review_by_forum_id(mysql_db, id)
        forum["review"] = review
        result.append(forum)
    return result

