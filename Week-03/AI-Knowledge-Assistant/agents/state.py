from typing import TypedDict,List,Dict,Any

class AgentState(TypedDict):

    question:str

    retrieved_documents:List[Dict[str,Any]]

    ranked_documents:List[Dict[str,Any]]

    answer:str

    sources:List[Dict[str,Any]]