from graph.state import GraphState

from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv
from langchain.schema import Document

def web_search(state: GraphState):
    """
    Retrieves the most relevant documents for the given state.
    
    Args:
        state: the current state of the graph
    
    Returns:
        A dictionary containing the most relevant documents
    """
    load_dotenv()

    question = state['question']
    documents = state['documents']

    web_search_tool = TavilySearchResults(max_results=3)

    web_search_results = web_search_tool.invoke(question)

    joined_results = "\n".join([result["content"] for result in web_search_results])

    web_results = Document(page_content = joined_results)

    if(documents is not None):
        documents.append(web_results)
    else:
        documents = [web_results]

    return {"documents": documents, "question": question}



