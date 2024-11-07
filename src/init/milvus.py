import db.milvus.repository as milvus_repository
import db.mysql.repository as mysql_repository

def initialize_milvus(mysql_db, milvus_collection):
    forum_list = mysql_repository.find_all_forum(mysql_db)
    print(len(forum_list))
    for forum in forum_list:
        milvus_repository.save_text(milvus_collection, forum["id"], forum["abstract"])
    print("[Milvus] initialized")