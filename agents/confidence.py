class ConfidenceEstimator:
    def __init__(self):
        pass

    def estimate(self, verification_info: dict, workflow_info: dict) -> dict:
        """
        Calculates a confidence score based on verification results.
        """
        missing = verification_info.get("missing", [])
        invalid = verification_info.get("invalid", [])
        workflow = workflow_info.get("workflow", [])
        
        if len(workflow) == 0:
            return {"confidence": 0.0}
            
        total_issues = len(missing) + len(invalid)
        
        # Simple heuristic: penalize confidence by 0.2 for every issue
        confidence = max(0.0, 1.0 - (total_issues * 0.2))
        
        return {
            "confidence": round(confidence, 2)
        }
