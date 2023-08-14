import streamlit as st
from sqlalchemy import create_engine
from langchain import OpenAI,SQLDatabase, SQLDatabaseChain
from langchain.llms import TextGen
import pandas as pd
import mysql.connector
import re
# Database connection configuration
db_username = "root"
db_password = "127.0.0.1"
db_hostname = "localhost"
db_port = "3306"
db_name = "sakila"

cnx = mysql.connector.connect(
    host=db_hostname,
    user=db_username,
    password=db_password,
    database=db_name
)

# Create a database connection
db = SQLDatabase.from_uri(f"mysql+pymysql://{db_username}:{db_password}@{db_hostname}:{db_port}/{db_name}")

# Streamlit app code
def execute_sql_query(question):
    llm = OpenAI(openai_api_key="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",temperature=0, verbose=True)
    db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True,return_direct=True,return_intermediate_steps=True)
    result = db_chain(question)
    response=result['intermediate_steps']
    sql_query = response[1]

    return sql_query, response[3]

def main():
    st.title("Sakila Actor Names")
    question = st.text_area("Show me all the actors that acted in movie id 26", height=100)

    # Execute the SQL query and display the result
    if st.button("Execute"):
        sql_query, query_result = execute_sql_query(question)
        sql_query = re.sub(r"SELECT\s+.*?\s+FROM", "SELECT * FROM", sql_query, flags=re.IGNORECASE)

        #Display the SQL query in a collapsible expander
        with st.expander("SQL Query", expanded=False):
            st.write(sql_query)
        cursor = cnx.cursor()
        cursor.execute(sql_query)
        # Fetch all the rows
        rows = cursor.fetchall()

if __name__ == "__main__":
    main()