from crewai import Agent
from textwrap import dedent
from langchain_google_genai import ChatGoogleGenerativeAI
from tool.nlp_processing_tool import NLPProcessingTool
from tool.routing_logic_tool import RoutingLogicTool


class HelpDeskAgents:
    def __init__(self, api_key: str):
        self.GeminiModel = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7, api_key=api_key)
        self.nlp_tool = NLPProcessingTool(api_key=api_key)
        self.routing_tool = RoutingLogicTool()
        print(f"NLP Tool: {self.nlp_tool}")
        print(f"Routing Tool: {self.routing_tool}")

    def router_agent(self):
        return Agent(
            role="Request Classifier",
            backstory=dedent("""Specializes in NLP-based intent detection. The Router Agent, known as 'Pulse', serves as the expert navigator for customer inquiries..."""),
            goal=dedent("Route inquiries to correct department"),
            tools=[self.nlp_tool, self.routing_tool],
            allow_delegation=False,
            verbose=True,
            llm=self.GeminiModel,
        )

    def tech_agent(self):
        return Agent(
            role="Network Specialist",
            backstory=dedent("""Expert in telecom infrastructure troubleshooting. The Tech Agent, 'Signal', embodies..."""),
            goal=dedent("Resolve 5G/network issues"),
            allow_delegation=False,
            verbose=True,
            llm=self.GeminiModel,
        )

    def billing_agent(self):
        return Agent(
            role="Billing Analyst",
            backstory=dedent("""Skilled in telecom billing systems. The Billing Agent, 'Ledger', focuses on demystifying..."""),
            goal=dedent("Resolve invoice disputes"),
            allow_delegation=False,
            verbose=True,
            llm=self.GeminiModel
        )
