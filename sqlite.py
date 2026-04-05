import streamlit as st
import sqlite3
import pandas as pd 
x = 3
st.write(x)
conn = sqlite3.connect('my_database.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS my_table
             (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
conn.commit()
c.execute("INSERT INTO my_table (name, age) VALUES ('Alice', 30)")
c.execute("INSERT INTO my_table (name, age) VALUES ('Bob', 25)")
conn.commit()
c.execute("SELECT * FROM my_table")
rows = c.fetchall()
df = pd.DataFrame(rows, columns=['id', 'name', 'age'])
st.write(df)
conn.close()