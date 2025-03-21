from typing import Dict, List, TypedDict, Any

from graph.state import GraphState

from graph.chain.retriever_grader import retrieval_grader



def grade_documents(state: GraphState) -> Dict[str,Any] :

    documents = state["documents"]
    question = state["question"]
    web_search = False
    newDoc = []

    if len(documents) == 0:
        web_search = True

    for d in documents: 
        response = retrieval_grader.invoke(
            {"question": question, "document": d.page_content}
        )
        if response.binary_score == 1:
            newDoc.append(d)
        else:
            web_search = True
            continue
    
    return {"documents": newDoc, "question": question, "web_search": web_search}

    