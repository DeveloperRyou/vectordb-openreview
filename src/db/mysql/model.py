import mysql.connector

def create_mysql_db():
    # MySQL 데이터베이스 연결 설정
    db = get_mysql_db()
    cursor = db.cursor(dictionary=True)

    # forum 테이블 생성
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS forum (
        id VARCHAR(255) NOT NULL PRIMARY KEY,
        title TEXT NOT NULL,
        abstract TEXT NOT NULL,
        authors TEXT NOT NULL,
        keywords TEXT NOT NULL,
        pdf VARCHAR(255) NOT NULL,
        invitation VARCHAR(255) NOT NULL,
        cdate TIMESTAMP NOT NULL
    )
    """)

    # review 테이블 생성
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS review (
        id VARCHAR(255) NOT NULL PRIMARY KEY,
        forum VARCHAR(255) NOT NULL,
        content TEXT NOT NULL,
        signatures VARCHAR(255) NOT NULL,
        invitation VARCHAR(255) NOT NULL,
        cdate TIMESTAMP NOT NULL,
        FOREIGN KEY (forum) REFERENCES forum(id)
    )
    """)

    print("[MySQL] database initialized")
    cursor.close()

    return db

def get_mysql_db():
    # MySQL 데이터베이스 연결 설정
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='openreview_db' 
    )
    return db