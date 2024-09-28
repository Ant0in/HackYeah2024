
from modules.legal_keywords_checker import LegalKeywordsChecker
from modules.trustpilot_checker import TrustPilotReviews
from modules.whois import WhoisLookupModule
from modules.update_date import UpdateDateModule

from pipeline import Pipeline
from executor import Executor
from networkx.drawing.nx_pydot import write_dot


pipeline = Pipeline()
pipeline.add_module("TrustPilotChecker", [])
pipeline.add_module("LegalChecker", [])
pipeline.add_module("WhoIS", [])
pipeline.add_module("UpdateDate", ["WhoIS"])

write_dot(pipeline.graph, "test.dot")


url: str = 'https://google.com'

module_list = {
    "TrustPilotChecker": TrustPilotReviews(url),
    "LegalChecker": LegalKeywordsChecker(url),
    "WhoIS": WhoisLookupModule(url),
    "UpdateDate": UpdateDateModule(),
}

executor = Executor()
executor.run_pipeline(pipeline, module_list)