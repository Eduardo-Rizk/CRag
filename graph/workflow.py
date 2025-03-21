from dotenv import load_dotenv


from langgraph.graph import END, StateGraph


from graph.nodes import retriever_node, gradeDocuments, web_search, generate
from graph.state import GraphState
from graph.consts import RETRIEVE, GENERATE, GRADE_DOCUMENTS, WEBSEARCH


load_dotenv()


def decide_to_generate(state):
    
    if state["web_search"]:
        return WEBSEARCH
    else:
        return GENERATE
    

workflow = StateGraph(GraphState)

workflow.add_node(RETRIEVE, retriever_node)
workflow.add_node(GRADE_DOCUMENTS, gradeDocuments)
workflow.add_node(WEBSEARCH, web_search)
workflow.add_node(GENERATE, generate)

workflow.set_entry_point(RETRIEVE)

workflow.add_edge(RETRIEVE, GRADE_DOCUMENTS)
workflow.add_conditional_edges(GRADE_DOCUMENTS, decide_to_generate)
workflow.add_edge(WEBSEARCH, GENERATE)

workflow.add_edge(GENERATE, END)

app = workflow.compile()

app.get_graph().draw_mermaid_png(output_file_path="graph.png")

if __name__ == "__main__":
    print(app.invoke(input={"question": "What is agent memory?"}))

