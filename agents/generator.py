class WorkflowGeneratorAgent:
    def __init__(self):
        pass

    def generate(self, tools_info: dict) -> dict:
        """
        Takes the selected tools and sequences them into a workflow.
        """
        tools = tools_info.get("tools", [])
        
        # Simulating workflow generation logic
        # For simplicity, we just keep the ordered sequence from tools, 
        # but in a real LLM this would involve creating a script or pipeline definition.
        workflow = tools.copy()
        
        return {
            "workflow": workflow
        }
