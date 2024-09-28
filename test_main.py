from modules.legal_keywords_checker import LegalKeywordsChecker
from pipeline import Pipeline
from executor import Executor

pipeline = Pipeline()
pipeline.add_module("LegalChecker", [])


module_list = {
    "LegalChecker": LegalKeywordsChecker("https://www.triathlonde.shop/"),
}

executor = Executor()
executor.run_pipeline(pipeline, module_list)