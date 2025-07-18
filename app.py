import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase


llm = ChatOpenAI(openai_api_key="OPEN_AI_KEY", model="gpt-4", temperature=0)


# Load the SQLite database
db = SQLDatabase.from_uri("sqlite:///Chinook.db")

# Create the SQL agent
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent_executor = create_sql_agent(llm=llm, toolkit=toolkit, verbose=False)

# Streamlit UI
st.title("SQL Chat with Chinook.db 🎵")

user_input = st.text_input("Ask a question about the database:")

if st.button("Submit") and user_input:
    with st.spinner("Thinking..."):
        try:
            response = agent_executor.run(user_input)
            st.success("Done!")
            st.markdown("### Result:")
            st.write(response)
        except Exception as e:
            st.error(f"Error: {e}")
