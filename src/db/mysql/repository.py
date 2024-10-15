import mysql.connector

def find_all_forum(db):
    try:
        cursor = db.cursor(dictionary=True)
        cursor.execute("""
        SELECT * FROM forum
        """)
        result = cursor.fetchall()
        cursor.close()
        return result
    except mysql.connector.Error as err:
        print(f"[Mysql] Error: {err}")

def find_forum_by_id(db, id):
    try:
        cursor = db.cursor(dictionary=True)
        cursor.execute("""
        SELECT * FROM forum WHERE id = %s
        """, (
            id,
        ))
        result = cursor.fetchall()
        cursor.close()
        return result[0]
    except mysql.connector.Error as err:
        print(f"[Mysql] Error: {err}")

def find_review_by_forum_id(db, forum_id):
    try:
        cursor = db.cursor(dictionary=True)
        cursor.execute("""
        SELECT * FROM review WHERE forum = %s
        """, (
            forum_id,
        ))
        result = cursor.fetchall()
        cursor.close()
        return result[0]
    except mysql.connector.Error as err:
        print(f"Error: {err}")
