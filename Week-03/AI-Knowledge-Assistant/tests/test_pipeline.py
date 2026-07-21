from rag.pipeline import ask_question


def test_ask_question():

    result=ask_question(
        "What is artificial intelligence?"
    )

    assert "question" in result
    assert "answer" in result
    assert "sources" in result
    assert "conversation_history" in result