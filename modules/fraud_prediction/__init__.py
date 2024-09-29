import numpy as np
import onnxruntime
import os



class FraudPrediction:

    MODEL_PATH: str = "./modules/fraud_prediction/model.onnx"

    def __init__(self, url: str) -> None:
        
        self.url: str = url

    def run(self, dependencies: list | None) -> dict:
        
        model_path: str = os.path.join(os.path.curdir, self.MODEL_PATH)
        # Initializing the ONNX Runtime session with the pre-trained model
        sess: onnxruntime.InferenceSession = onnxruntime.InferenceSession(
            self.MODEL_PATH,
            providers=["CPUExecutionProvider"],
        )

        input_url: np.array = np.array([self.url], dtype="str")

        # Using the ONNX model to make predictions on the input data
        results = sess.run(None, {"inputs": input_url})[1]
        prob_safe: float = results[0][0]
        return {'score': float(prob_safe)}



if __name__ == '__main__':
    print(FraudPrediction(url='https://www.google.com').run([]))