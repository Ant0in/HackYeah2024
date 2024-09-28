from datetime import datetime, timezone
import math

class UpdateDateModule:

    def __init__(self):
        ...

    def run(self, dependencies: list):
        
        whois_dep = dependencies[0]
        last_update: list | str = whois_dep.get('updated_date')

        if isinstance(last_update, list): last_update = last_update[-1]
        else: return {'score': 0.5}

        now = datetime.now(timezone.utc)
        
        # Vérifie si last_update a une timezone. Sinon, force-le à UTC.
        if last_update.tzinfo is None:
            # Considérer last_update comme étant en UTC s'il n'a pas de tzinfo
            last_update = last_update.replace(tzinfo=timezone.utc)
        
        # Calcule la différence entre maintenant (UTC) et last_update
        delta = now - last_update
        
        # Calculer le nombre de jours entre ces deux dates
        return {
            'score': -math.exp(-((delta.days/100)**2)) + 1,
            'last_update': last_update
        }