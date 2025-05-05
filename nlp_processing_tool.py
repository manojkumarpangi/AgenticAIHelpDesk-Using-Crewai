from langchain_google_genai import ChatGoogleGenerativeAI
from tool.base_tool import BaseTool  # Import the BaseTool

class NLPProcessingTool(BaseTool):
    def __init__(self, api_key: str):
        super().__init__()  # Call the base class initializer
        # Initialize the model with the desired parameters
        self.model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7, api_key=api_key)

    def analyze_query(self, query: str) -> dict:
        prompt = f"Identify the intent of the following query: '{query}' and return a structured output like {{'intent': 'billing', 'confidence': 0.95}}."
        
        # Use the model's chat method for generating a response
        response = self.model.chat([{"role": "user", "content": prompt}])
        
        try:
            # Assuming the response is returned as a string, you may need to parse it accordingly
            structured_response = eval(response['content'])  # Be cautious with eval
            return structured_response
        except Exception as e:
            print(f"Error parsing response: {e}")
            return {"intent": "unknown", "confidence": 0.0}  # Fallback output
        
    def execute(self, query: str):
        """Override the execute method to analyze queries."""
        return self.analyze_query(query)
