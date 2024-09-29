
from modules.legal_keywords_checker import LegalKeywordsChecker
from modules.trustpilot_checker import TrustPilotReviews
from modules.whois import WhoisLookupModule
from modules.update_date import UpdateDateModule
from modules.media import MediaModule
from modules.html_parser import HTMLParserModule
from modules.html_text import HTMLTextModule
from modules.type_checker import ThemeChecker
from modules.fraud_prediction import FraudPrediction
from modules.chatgpt_prediction import ChatGPTPrediction

from pipeline import Pipeline
from executor import Executor
from db import DB



pipeline = Pipeline()
#pipeline.add_module('ChatGPTPrediction', ['HTMLTextModule', 'ThemeChecker'])
pipeline.add_module('FraudPrediction', [])
pipeline.add_module('HTMLParser', [])
pipeline.add_module('HTMLTextModule', ['HTMLParser'])
pipeline.add_module("LegalChecker", [])
pipeline.add_module("MediaModule", ["HTMLParser"])
pipeline.add_module("TrustPilotChecker", ["HTMLTextModule"])
pipeline.add_module('ThemeChecker', ["HTMLTextModule"])
pipeline.add_module("UpdateDate", ["WhoIS"])
pipeline.add_module("WhoIS", [])


url: str = r'https://hackyeah.pl/'

module_list = {
    #"ChatGPTPrediction": ChatGPTPrediction(url),
    "FraudPrediction": FraudPrediction(url),
    "HTMLParser": HTMLParserModule(url),
    "HTMLTextModule": HTMLTextModule(url),
    "LegalChecker": LegalKeywordsChecker(url),
    "MediaModule": MediaModule(url),
    "TrustPilotChecker": TrustPilotReviews(url),
    "ThemeChecker": ThemeChecker(url, 'polish'),
    "UpdateDate": UpdateDateModule(),
    "WhoIS": WhoisLookupModule(url),

}


executor = Executor()
score: float = executor.run_pipeline(pipeline, module_list)
DB(path='./dd.db').put_website(url=url, score=score)