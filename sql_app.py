# from dotenv import load_dotenv
# load_dotenv()  #load all the environment variables

# import streamlit as st
# import os
# import sqlite3

# import google.generativeai as genai

# #configure our api key
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# #function to load google gemini model and provide sql query as response
# def get_gemini_response(question,prompt):
#     model = genai.GenerativeModel("gemini-pro")
#     response = model.generate_content([prompt,question])
#     return response.text

# #Function to retrieve query from the sql database
# def read_sql_query(sql,db):
#     conn = sqlite3.connect(db)
#     cur = conn.cursor()
#     cur.execute(sql)
#     rows = cur.fetchall()
#     conn.commit()
#     conn.close()
#     for row in rows:
#         print(row)
#     return rows

# #define your prompt
# prompt= ["""
# you are an expert in converting English questions to sql query!
# The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION and MARKS \n\n For example, \nexample1 - How many entries of records are present the SQL command will be something like this SELECT COUNT(*) FROM STUDENT; \nexample 2 - Tell me all the students studying in Data sci class?,
# the SQL command will be something like this SELECT * FROM STUDENT where CLASS="Data sci";
#          also the sql code should not have ''' in the beginning or end and sql word in the output.
# """]


# #streamlit app

# st.set_page_config(page_title="I can retrieve any SQL query")
# st.header("Gemini App To Retrieve SQL Data")

# question = st.text_input("Ask the question")

# submit = st.button("Ask the question")

# #if submit is clicked
# if submit:
#     response = get_gemini_response(question,prompt)
#     print(response)
#     data = read_sql_query(response,"student.db")
#     st.subheader("The response is")
#     for row in data:
#         print(row)
#         st.header(row)








# from dotenv import load_dotenv
# import streamlit as st
# import os
# import sqlite3
# import google.generativeai as genai

# # Load environment variables
# load_dotenv()

# # Configure Google Gemini API key
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Function to load Google Gemini model and provide SQL query as response
# def get_gemini_response(question):
#     model = genai.GenerativeModel("gemini-pro")
#     prompt = """
#     You are an expert in converting English questions to SQL queries!
#     The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION, and MARKS.
#     For example:
#     - How many entries of records are present? The SQL command will be something like this: SELECT COUNT(*) FROM STUDENT;
#     - Tell me all the students studying in data sci class. The SQL command will be something like this: SELECT * FROM STUDENT WHERE CLASS="Data sci";
#     The SQL code should not have ''' in the beginning or end and should not include the word SQL in the output.
#     """
#     response = model.generate_content(prompt + " " + question)
#     return response.text.strip()  # Ensure trailing spaces are removed

# # Function to retrieve data from the SQL database
# def read_sql_query(sql, db):
#     conn = sqlite3.connect(db)
#     cur = conn.cursor()
#     cur.execute(sql)
#     rows = cur.fetchall()
#     conn.close()
#     return rows

# # Streamlit app
# st.set_page_config(page_title="SQL Query Generator App")
# st.header("Gemini App To Retrieve SQL Data")

# # Input field and button
# question = st.text_input("Ask the question")
# submit = st.button("Submit")

# # If the button is clicked
# if submit:
#     response = get_gemini_response(question)
#     st.write("Generated SQL Query:", response)

#     # Execute the SQL query and display results
#     try:
#         data = read_sql_query(response, "student.db")
#         st.subheader("The response is:")
#         for row in data:
#             st.write(row)  # Display each row of data
#     except Exception as e:
#         st.error(f"An error occurred: {e}")









from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini model and provide SQL query as response
def get_gemini_response(question):
    model = genai.GenerativeModel("gemini-pro")
    prompt = """
    You are an expert in converting English questions to SQL queries!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION, and MARKS.
    For example:
    - How many entries of records are present? The SQL command will be something like this: SELECT COUNT(*) FROM STUDENT;
    - Tell me all the students studying in Data sci class. The SQL command will be something like this: SELECT * FROM STUDENT WHERE CLASS="Data sci";
    The SQL code should not have ''' in the beginning or end and should not include the word SQL in the output.
    """
    response = model.generate_content(prompt + " " + question)
    return response.text.strip()  # Ensure trailing spaces are removed

# Function to retrieve data from the SQL database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    try:
        cur.execute(sql)
        rows = cur.fetchall()
    except sqlite3.Error as e:
        rows = []
        st.error(f"SQL Error: {e}")
    finally:
        conn.close()
    return rows

# Streamlit app
st.set_page_config(page_title="SQL Query Generator App")
st.header("Harsh App To Retrieve SQL Data")

# Input field and button
question = st.text_input("Ask the question")
submit = st.button("Submit")

# If the button is clicked
if submit:
    if not question:
        st.error("Please enter a question.")
    else:
        response = get_gemini_response(question)
        st.write("Generated SQL Query:", response)

        # Execute the SQL query and display results
        data = read_sql_query(response, "student.db")
        if data:
            st.subheader("The response is:")
            for row in data:
                st.write(row)  # Display each row of data
        else:
            st.write("No data found or error executing query.")

