import db.milvus.model as milvus_model
import db.mysql.model as mysql_model

import init.pdf as init_pdf

if __name__ == "__main__":
    milvus_collection = milvus_model.create_milvus_db()
    mysql_db = mysql_model.create_mysql_db()
    init_pdf.initialize_pdf(mysql_db)