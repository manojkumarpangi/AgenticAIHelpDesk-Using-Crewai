import os
from crewai import Crew
from textwrap import dedent
from agents import HelpDeskAgents
from tasks import HelpDeskTasks


class CustomCrew:
    def __init__(self, query: str, api_key: str):
        self.query = query
        self.agents = HelpDeskAgents(api_key=api_key)
        self.tasks = HelpDeskTasks()

    def create_agents(self):
        return [self.agents.router_agent(), self.agents.tech_agent(), self.agents.billing_agent()]

    def create_tasks(self):
        tasks = [
            self.tasks.route_task(self.agents.router_agent(), self.query),
            self.tasks.tech_support_task(self.agents.tech_agent(), self.query),
            self.tasks.billing_task(self.agents.billing_agent(), self.query)
        ]
        return tasks

    def run(self):
        crew = Crew(
            agents=self.create_agents(),
            tasks=self.create_tasks(),
            verbose=True,
        )
        result = crew.kickoff()
        if not result:
            print("Failed to execute crew tasks.")
        return result


if __name__ == "__main__":
    print("## Welcome to Crew AI Help Desk!")
    print("-------------------------------")
    try:
        query = input(dedent("""Enter Your Concern Here: """))
    except Exception as e:
        print("Error reading input:", e)
        query = ""

    # Load the API key from an environment variable
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        raise ValueError("API key for Gemini is not set in the environment variables.")
    
    custom_crew = CustomCrew(query, api_key)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is your custom crew run result:")
    print("########################\n")
    print(result)
