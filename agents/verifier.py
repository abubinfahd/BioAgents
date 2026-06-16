class VerificationAgent:
    def __init__(self):
        # The verifier has access to gold standard rules or ontological requirements
        self.rules = {
            "Differential Expression": ["FastQC", "STAR", "featureCounts", "DESeq2"],
            "Variant Calling": ["FastQC", "BWA", "Samtools", "GATK", "VCF Output"],
            "Protein Analysis": ["BLAST", "Clustal Omega", "Phylogenetic Analysis"]
        }

    def verify(self, workflow_info: dict, task_info: dict) -> dict:
        """
        Checks the generated workflow against domain rules.
        """
        workflow = workflow_info.get("workflow", [])
        task = task_info.get("task", "")
        
        expected_steps = self.rules.get(task, [])
        missing_steps = [step for step in expected_steps if step not in workflow]
        invalid_steps = [step for step in workflow if step not in expected_steps]
        
        is_valid = len(missing_steps) == 0 and len(invalid_steps) == 0
        
        return {
            "valid": is_valid,
            "missing": missing_steps,
            "invalid": invalid_steps
        }
