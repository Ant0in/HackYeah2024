import datetime
import math

class UpdateDateModule:

    def __init__(self):
        ...

    def run(self, dependencies: list):
        
        whois_dep = dependencies[0]
        
        last_update: datetime.date = whois_dep["updated_date"] 
        now = datetime.date.today()
        delta = now - last_update
        # Get number of days between those two dates
        return {
            'score': -math.exp(-((delta.days/100)**2)) + 1,
            'last_update': last_update
        }