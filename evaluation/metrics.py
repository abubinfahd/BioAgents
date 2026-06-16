import json

class MetricsEvaluator:
    def __init__(self):
        pass

    def calculate_workflow_accuracy(self, generated_workflow: list, gold_workflow: list) -> float:
        """
        Calculates F1 score based on overlapping steps.
        """
        if not generated_workflow or not gold_workflow:
            return 0.0
            
        gen_set = set(generated_workflow)
        gold_set = set(gold_workflow)
        
        true_positives = len(gen_set.intersection(gold_set))
        false_positives = len(gen_set - gold_set)
        false_negatives = len(gold_set - gen_set)
        
        precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
        recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0
        
        if precision + recall == 0:
            return 0.0
            
        f1 = 2 * (precision * recall) / (precision + recall)
        return round(f1, 2)

    def calculate_completeness(self, generated_workflow: list, gold_workflow: list) -> float:
        """
        Detected Steps / Required Steps
        """
        if not gold_workflow:
            return 1.0
        
        detected = len(set(generated_workflow).intersection(set(gold_workflow)))
        return round(detected / len(gold_workflow), 2)

    def calculate_hallucination_rate(self, generated_workflow: list, gold_workflow: list) -> float:
        """
        Invalid Tools / Generated Tools
        """
        if not generated_workflow:
            return 0.0
            
        invalid = len(set(generated_workflow) - set(gold_workflow))
        return round(invalid / len(generated_workflow), 2)

    def evaluate(self, generated_workflow: list, gold_workflow: list) -> dict:
        return {
            "accuracy_f1": self.calculate_workflow_accuracy(generated_workflow, gold_workflow),
            "completeness": self.calculate_completeness(generated_workflow, gold_workflow),
            "hallucination_rate": self.calculate_hallucination_rate(generated_workflow, gold_workflow)
        }
