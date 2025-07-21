# mcp/bus.py
class MCPBus:
    def __init__(self):
        self.agents = {}

    def register(self, name, handler):
        self.agents[name] = handler

    def send(self, message):
        receiver = message["receiver"]
        if receiver in self.agents:
            return self.agents[receiver](message)
        else:
            raise ValueError(f"Unknown agent: {receiver}")
