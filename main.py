from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase


db = SQLDatabase.from_uri("sqlite:///Chinook.db")

# Set up the LLM with environment variable
llm = ChatOpenAI(openai_api_key="OPEN_AI_KEY", model="gpt-4", temperature=0)

# Set up the agent
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent_executor = create_sql_agent(llm=llm, toolkit=toolkit, verbose=True)

# Ask a query
while True:
    user_input = input("Ask a question (or type 'exit'): ")
    if user_input.lower() == "exit":
        break
    response = agent_executor.run(user_input)
    print(response)
