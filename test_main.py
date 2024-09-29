
from modules.legal_keywords_checker import LegalKeywordsChecker
from modules.trustpilot_checker import TrustPilotReviews
from modules.whois import WhoisLookupModule
from modules.update_date import UpdateDateModule
from modules.media import MediaModule
from modules.html_parser import HTMLParserModule
from modules.html_text import HTMLTextModule
from modules.type_checker import ThemeChecker
from modules.fraud_prediction import FraudPrediction

from pipeline import Pipeline
from executor import Executor



pipeline = Pipeline()
pipeline.add_module('FraudPrediction', [])
pipeline.add_module('HTMLParser', [])
pipeline.add_module('HTMLTextModule', ['HTMLParser'])
pipeline.add_module("LegalChecker", [])
pipeline.add_module("MediaModule", ["HTMLParser"])
# rev image
#pipeline.add_module("TrustPilotChecker", ["HTMLTextModule"])
pipeline.add_module('ThemeChecker', ["HTMLTextModule"])
pipeline.add_module("UpdateDate", ["WhoIS"])
pipeline.add_module("WhoIS", [])


url: str = 'https://www.penoblode.shop/'

module_list = {
    "FraudPrediction": FraudPrediction(url),
    "HTMLParser": HTMLParserModule(url),
    "HTMLTextModule": HTMLTextModule(url),
    "LegalChecker": LegalKeywordsChecker(url),
    "MediaModule": MediaModule(url),
    # rev image
    #"TrustPilotChecker": TrustPilotReviews(url),
    "ThemeChecker": ThemeChecker(url, 'polish'),
    "UpdateDate": UpdateDateModule(),
    "WhoIS": WhoisLookupModule(url),
}


executor = Executor()
score: float = executor.run_pipeline(pipeline, module_list)
print(score)