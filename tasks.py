from crewai import Task
from textwrap import dedent


class HelpDeskTasks:
    TIP_SECTION = "If you do your BEST WORK, you will be rewarded with the $10,000 commission."

    def route_task(self, router_agent, query):
        try:
            analysis_result = router_agent.nlp_tool.analyze_query(query)
            department = router_agent.routing_tool.route_query(analysis_result)
            if not department:
                print("Error: No valid department found.")
                return Task(...)  # Handle error appropriately

            print(f"Routing to department: {department}")
            return Task(
                description=dedent(f"""
                    **Task**: Analyze the incoming customer query: "{query}".
                    **Description**: Use advanced natural language understanding to determine the underlying intent...
                    **Parameters**:
                    -- `query`: The customer query to be analyzed. {query}
                    -- `router_agent`: The agent responsible for routing the query to the appropriate department.

                    **Tip**: {self.TIP_SECTION}
                """),
                expected_output="Department or the agent name to which the ticket needs to be assigned (tech/billing): {department}",
                agent=router_agent,
            )
        except Exception as e:
            print(f"Error processing route task: {e}")
            return Task(...)  # Handle error appropriately

    def tech_support_task(self, tech_agent, query):
        return Task(
            description=dedent(f"""
                **Task**: Take the incoming customer query and analyze it for common network issues.
                **Description**: Use your expertise in telecom infrastructure to identify potential problems...
                **Parameters**:
                -- `query`: The customer query to be analyzed. {query}
                -- `tech_agent`: The agent responsible for technical support.

                **Tip**: {self.TIP_SECTION}
            """),
            expected_output="Diagnostic results for network issues.",
            agent=tech_agent,
        )

    def billing_task(self, billing_agent, query):
        return Task(
            description=dedent(f"""
                **Task**: Take the incoming customer query and analyze it for billing-related issues.
                **Description**: Use your expertise in telecom billing systems to identify potential problems...
                **Parameters**:
                -- `query`: The customer query to be analyzed. {query}
                -- `billing_agent`: The agent responsible for billing support.

                **Tip**: {self.TIP_SECTION}
            """),
            expected_output="Billing-related issue resolution.",
            agent=billing_agent,
        )
