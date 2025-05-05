from tool.base_tool import BaseTool  # Import the BaseTool

class RoutingLogicTool(BaseTool):
    def __init__(self):
        super().__init__()  # Call the base class initializer

    def route_query(self, analysis_result):
        intent = analysis_result.get('intent')
        if intent == 'billing':
            return 'billing_agent'
        elif intent == 'technical':
            return 'tech_agent'
        else:
            return 'general_inquiry_agent'  # Fallback for unrecognized intents
        
    def execute(self, request: str):
        """Override the execute method to route requests."""
        return self.route_query(request)
