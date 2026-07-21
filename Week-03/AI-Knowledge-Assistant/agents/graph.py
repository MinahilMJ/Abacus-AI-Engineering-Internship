from langgraph.graph import StateGraph,START,END

from agents.state import AgentState
from agents.nodes import (
    retrieve_node,
    rerank_node,
    generate_node
)

workflow=StateGraph(
    AgentState
)

workflow.add_node(
    "retrieve",
    retrieve_node
)

workflow.add_node(
    "rerank",
    rerank_node
)

workflow.add_node(
    "generate",
    generate_node
)

workflow.add_edge(
    START,
    "retrieve"
)

workflow.add_edge(
    "retrieve",
    "rerank"
)

workflow.add_edge(
    "rerank",
    "generate"
)

workflow.add_edge(
    "generate",
    END
)

agent=workflow.compile()

def ask_agent(question):

    result=agent.invoke(
        {
            "question":question
        }
    )

    return {
        "question":question,
        "answer":result.get(
            "answer",
            ""
        ),
        "sources":result.get(
            "sources",
            []
        )
    }