from modules.legal_keywords_checker import LegalKeywordsChecker
from modules.trustpilot_checker import TrustPilotReviews
from pipeline import Pipeline
from executor import Executor, ParallelExecutor

pipeline = Pipeline()
pipeline.add_module("TrustPilotChecker", [])
pipeline.add_module("LegalChecker", [])


url: str = 'https://google.com'

module_list = {
    "TrustPilotChecker": TrustPilotReviews(url),
    "LegalChecker": LegalKeywordsChecker(url),
}

executor = Executor()
executor.run_pipeline(pipeline, module_list)