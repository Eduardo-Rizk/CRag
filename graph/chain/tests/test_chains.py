from dotenv import load_dotenv

load_dotenv()


from graph.chain.retriever_grader import GradeDocuments, retrieval_grader
from graph.chain.generation import generation_chain
from ingestion import retriever


def test_retrieval_upcase():

    question = "agent memory"

    docs = retriever.invoke(question)

    doc_txt = docs[1].page_content


    response = retrieval_grader.invoke(
        {"question": question, "document": doc_txt}
    )

    assert response.binary_score == 1

def test_generation():

    question = "agent memory"

    docs = retriever.invoke(question)

    generation = generation_chain.invoke(
        {"question": question, "context": docs}
    )

    print(generation)

    