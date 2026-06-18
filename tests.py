#DANGEROUS
import sqlite3

def login_unsafe(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    
    return cursor.fetchone()

import sqlite3

def search_user_unsafe(name):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    cursor.execute(query)
    
    return cursor.fetchall()

import mysql.connector

def get_user_data_unsafe(user_id):
    conn = mysql.connector.connect(host='localhost', database='mydb')
    cursor = conn.cursor()
    
    query = "SELECT * FROM users WHERE id = %s" % user_id
    cursor.execute(query)
    
    return cursor.fetchall()


#SAFE
import sqlite3

def search_user_safe(name):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    query = "SELECT * FROM users WHERE name = :name"
    cursor.execute(query, {"name": name})
    
    return cursor.fetchall()

from sqlalchemy import create_engine, text

def delete_record_safe(record_id):
    engine = create_engine('postgresql://user:pass@localhost/db')
    
    with engine.connect() as conn:
        query = text("DELETE FROM users WHERE id = :id")
        conn.execute(query, {"id": record_id})
        conn.commit()
