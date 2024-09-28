
from modules.legal_keywords_checker import LegalKeywordsChecker
from modules.trustpilot_checker import TrustPilotReviews
from modules.whois import WhoisLookupModule
from modules.update_date import UpdateDateModule
from modules.media import MediaModule
from modules.html_parser import HTMLParserModule


from pipeline import Pipeline
from executor import Executor


pipeline = Pipeline()
#pipeline.add_module("TrustPilotChecker", [])
pipeline.add_module("LegalChecker", [])
pipeline.add_module("WhoIS", [])
pipeline.add_module("UpdateDate", ["WhoIS"])
pipeline.add_module('HTMLParser', [])
pipeline.add_module("MediaModule", ["HTMLParser"])


url: str = 'https://www.biedronka.pl/pl'

module_list = {
    #"TrustPilotChecker": TrustPilotReviews(url),
    "LegalChecker": LegalKeywordsChecker(url),
    "WhoIS": WhoisLookupModule(url),
    "UpdateDate": UpdateDateModule(),
    "HTMLParser": HTMLParserModule(url),
    "MediaModule": MediaModule(url),
}

executor = Executor()
executor.run_pipeline(pipeline, module_list)