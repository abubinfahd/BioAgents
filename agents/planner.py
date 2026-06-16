class PlannerAgent:
    def __init__(self):
        # In a real system, this would hold the LLM client
        pass

    def plan(self, query: str) -> dict:
        """
        Takes a user query and returns a structured task object.
        """
        task_mapping = {
            "differentially expressed genes": "Differential Expression",
            "RNA-seq": "Differential Expression",
            "VCF": "Variant Calling",
            "variant calling": "Variant Calling",
            "phylogenetic analysis": "Protein Analysis",
            "Protein sequences": "Protein Analysis"
        }
        
        detected_task = "Unknown Task"
        for key, task in task_mapping.items():
            if key.lower() in query.lower():
                detected_task = task
                break
                
        return {
            "task": detected_task,
            "original_query": query
        }
