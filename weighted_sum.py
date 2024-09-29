
class WeightedSum:

    weights: dict = {
        'FraudPrediction': 3,
        'LegalChecker': 1,
        'MediaModule': 2,
        'UpdateDate': 1.5,
        'ChatGPTPrediction': 1
    }

    @staticmethod
    def calculateWeightedSum(scores: dict) -> float:

        weighted_sum = sum([s * WeightedSum.weights[w] for w, s in scores.items()])
        total_weights = sum([WeightedSum.weights[w] for w in scores.keys()])
        
        return round(weighted_sum / total_weights, 4) if total_weights != 0 else 0


if __name__ == '__main__':
    vec = {'FraudPrediction': 0.935395359992981, 'LegalChecker': 0.5, 'MediaModule': 1, 'UpdateDate': 0.9999594266860768}
    print(WeightedSum.calculateWeightedSum(vec))
