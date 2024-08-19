from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
import os
from dotenv import load_dotenv

load_dotenv()

def setup_qa_system(docsearch):
    llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.7)

    custom_prompt_template = """
    You are an expert NFL data analyst. You will be provided with NFL data, and your job is to perform an advanced analysis that includes winning percentages, player performance, team standings, trades, and more. Your analysis should offer detailed insights based on the provided data.

### Data Analysis Task:

    {context}

    Now, based on this information, answer the following question:

    {question}
    1. Winning Predictions: Estimate the winning percentage for the player or team based on past performance and current statistics.
    2. Team and Player Insights: Analyze the performance of teams, players, and trades in the current NFL season.
    3. Current Scenario: Provide insights on how the current season trends affect future games, playoffs, or trades.
    4. Data Visualization (if needed):
        - Chart Type (e.g., bar chart, line chart, scatter plot)
        - Key Data Points (comma-separated)
        - Axis Labels (x and y axes)
        - Chart Title
   5. Summary: Provide a concise analysis and actionable recommendations based on the NFL data.
   
   Deliver an expert analysis below:
    """

    prompt = PromptTemplate(template=custom_prompt_template, input_variables=['context', 'question'])

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type='stuff',
        retriever=docsearch.as_retriever(search_type="similarity", search_kwargs={"k":2}),
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True
    )

    return qa
