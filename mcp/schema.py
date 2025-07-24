#schema
def build_mcp_message(sender, receiver, type_, trace_id, payload):
    return {
        "sender": sender,
        "receiver": receiver,
        "type": type_,
        "trace_id": trace_id,
        "payload": payload,
    }
