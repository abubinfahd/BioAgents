class ToolSelectorAgent:
    def __init__(self):
        # Database of domain tools
        self.tool_database = {
            "Differential Expression": ["FastQC", "Trimmomatic", "STAR", "featureCounts", "DESeq2", "edgeR", "Salmon"],
            "Variant Calling": ["FastQC", "BWA", "Samtools", "GATK", "FreeBayes", "VCF Output"],
            "Protein Analysis": ["BLAST", "Clustal Omega", "Phylogenetic Analysis", "HMMER"]
        }

    def select_tools(self, task_info: dict) -> dict:
        """
        Takes the planned task and selects relevant tools.
        """
        task = task_info.get("task", "")
        available_tools = self.tool_database.get(task, [])
        
        # Simulating LLM tool selection by returning a subset (sometimes hallucinating or missing tools)
        selected_tools = []
        if task == "Differential Expression":
            selected_tools = ["FastQC", "STAR", "DESeq2"] # intentionally missing featureCounts
        elif task == "Variant Calling":
            selected_tools = ["FastQC", "BWA", "GATK", "VCF Output"] # missing Samtools
        elif task == "Protein Analysis":
            selected_tools = ["BLAST", "Clustal Omega", "Phylogenetic Analysis"]
        else:
            selected_tools = ["UnknownTool"]

        return {
            "tools": selected_tools
        }
