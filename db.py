import sqlite3

def get_user_info(username):
    # 🔥 Requête SQL vulnérable (injection SQL)
    query = f"SELECT * FROM users WHERE username = '{username}'"
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()
