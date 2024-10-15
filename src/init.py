import db.milvus.model as milvus_model
import db.milvus.repository as milvus_repository
import db.mysql.model as mysql_model
import db.mysql.repository as mysql_repository

milvus_collection = milvus_model.create_milvus_db()
mysql_db = mysql_model.create_mysql_db()

def initialize_milvus():
    forum_list = mysql_repository.find_all_forum(mysql_db)
    print(len(forum_list))
    for forum in forum_list:
        milvus_repository.save_text(milvus_collection, forum["id"], forum["abstract"])
    print("[Milvus] initialized")

if __name__ == "__main__":
    initialize_milvus()