from agents.ingestion_agent import handle_ingestion
from agents.retrieval_agent import handle_retrieval
from agents.llm_response_agent import handle_llm_response
from mcp.bus import MCPBus
from mcp.schema import build_mcp_message

bus = MCPBus()

def register_agents():
    bus.register("IngestionAgent", handle_ingestion)
    bus.register("RetrievalAgent", handle_retrieval)
    bus.register("LLMResponseAgent", handle_llm_response)
    bus.register("CoordinatorAgent", handle_coordinator)

def handle_coordinator(message):
    
    return message
