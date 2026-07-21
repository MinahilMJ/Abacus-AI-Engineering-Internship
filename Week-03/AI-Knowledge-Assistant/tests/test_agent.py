from agents.graph import agent


def test_agent():

    result=agent.invoke(
        {
            "question":"What is artificial intelligence?"
        }
    )

    assert result["answer"]

    assert len(
        result["sources"]
    )>0