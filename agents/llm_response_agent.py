from utils.llm import call_openai_chat
from mcp.schema import build_mcp_message

def handle_llm_response(message):
    context = "\n\n".join(message["payload"]["top_chunks"])
    query = message["payload"]["query"]
    answer = call_openai_chat(context, query)

    return build_mcp_message(
        "LLMResponseAgent", "CoordinatorAgent", "FINAL_ANSWER", message["trace_id"],
        {"answer": answer, "chunks": message["payload"]["top_chunks"]}
    )
