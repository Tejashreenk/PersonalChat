import sqlite3
import random
import string
import openai
from openai import OpenAI
import os
from getpass import getpass

class SQL_Answer_Agent:
    def __init__(self, client) -> None:
        # TODO: Initialize the client and prompt for the Obnoxious_Agent
        self.client = client
        self.schema = None

    def set_prompt(self, question, prompt=None):
        # TODO: Set the prompt for the Obnoxious_Agent
        if prompt:
            self.prompt = prompt
        else:
            self.prompt = f"Use the schema {self.schema} and Respond ONLY with sqlite query to get answer to the question:{question}"

    # def set_schema(self, question, prompt=None):
    #     # TODO: Set the prompt for the Obnoxious_Agent
    #     if prompt:
    #         self.prompt = prompt
    #     else:
    #         self.prompt = f"Respond ONLY with sqlite query to get answer to the question:{question}"

    # Function to print the schema of the database using sqlite_master
    def get_set_db_schema(self):
        cursor.execute("SELECT sql FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        self.schema = tables
        # prompt = f"Schema for db: {tables}"
        # response = self.set_schema_context_openai(prompt)
        # for table in tables:
        #     print(table[0])
        return True
 
    def execute_sql_query(self, question, response) -> bool:
        # TODO: Extract the action from the response
        if response:
            print(response)
            cursor.execute(f"""{response}""")
            rows = cursor.fetchall()
            print(rows)
            response = self.summarize_sql_response(f"Question: {question} Answer: {rows}")
            return response
        else:
            return False

    def set_schema_context_openai(self,prompt):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    def get_answer(self, query, prompt=None):
        if prompt:
            prompt = prompt
        else:
            prompt = f"Use the schema {self.schema} and Respond ONLY with sqlite query to get answer to the question:{query}"
            
        # TODO: Check if the query is obnoxious or not
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return self.execute_sql_query(query, response.choices[0].message.content)

    def print_query_results(rows):
        for row in rows:
            print(row)

    def summarize_sql_response(self, sql_response):
        self.prompt = f"Summarize:{sql_response}"        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": self.prompt}]
        )
        summary = response.choices[0].message.content
        return summary

# Connect to the SQLite database
conn = sqlite3.connect('MyCompany.db')
cursor = conn.cursor()

def setup_openai():
    """
    Setup OpenAI with the provided API key.
    
    Returns:
    OpenAI client object.
    """
    if "OPENAI_API_KEY" not in os.environ:
        os.environ["OPENAI_API_KEY"] = getpass("Enter OPENAI_API_KEY: ") 
        
    # Initialize OpenAI client
    openai.api_key = os.environ["OPENAI_API_KEY"]
    
    return openai

def get_query_response_from_openai():

    setup_openai()
    # Set OpenAI client
    openAI_client = OpenAI(api_key=openai.api_key)
    sql_agent = SQL_Answer_Agent(openAI_client)
    is_schema_set = sql_agent.get_set_db_schema()
    print(is_schema_set)

    answer = sql_agent.get_answer("give me details of employees in Irwin-Martinez company?")
    print("############")
    print(answer)

if __name__ == "__main__":
    get_query_response_from_openai()
    cursor = conn.close()
