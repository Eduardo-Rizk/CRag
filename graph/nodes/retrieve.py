from graph.state import GraphState
from ingestion import retriever
from typing import Any , Dict


def retriever_node(state: GraphState) -> Dict[str, Any]:
    """
    Retrieves the most relevant documents for the given state.
    
    Args:
        state: the current state of the graph
    
    Returns:
        A dictionary containing the most relevant documents
    """
    question = state['question']

    docs = retriever.invoke(question)

    return {"documents": docs, "question": question}




