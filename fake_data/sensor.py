import numpy as np
from datetime import date, timedelta
import sys

class sensor_visit:
    """
    Simule un sensor d'entrée de porte;
    Prend en paramètre une moyenne et un écart-type,
    retourne le nombre de visiturs qui sont
    passés par la porte à une date donnée
    """

    def __init__(self, avg_visit: int, std_visit: int, perc_break : float = 0.015, perc_malfunction : float = 0.035) -> None:
        self.avg_visit = avg_visit
        self.std_visit = std_visit
        self.perc_break = perc_break
        self.perc_malfunction = perc_malfunction

    def simulate_visit(self, business_date: date) -> int:
        """
        Simule le nombre de visiturs
        """

        np.random.seed(seed = business_date.toordinal())

        week_day = business_date.weekday()

        # Déclaration de la loi normale à suivre pour notre simulation de données
        visit = np.random.normal(self.avg_visit, self.std_visit)

        # Modifications du nombre de visits selon les jours
        if week_day == 2:
            visit *= 1.10
        if week_day == 4:
            visit *= 1.27
        if week_day == 5:
            visit *= 1.35

        # Magasin fermé le dimanche
        if week_day == 6:
            visit = -1

        if business_date.month == 5 and business_date.day == 1:
            visit = 0

        return np.floor(visit)

    def get_visit_count(self, business_date: date) -> int:
        """
        Retourne le nombre de visiturs
        """

        np.random.seed(seed = business_date.toordinal())
        proba_malfunction = np.random.random()

        # Possibilité que le sensor casse
        if proba_malfunction < self.perc_break:
            return 0

        visit = self.simulate_visit(business_date)

        # Le sensor fonctionne mal - détecte une personne sur 5
        if proba_malfunction < self.perc_malfunction:
            visit = np.floor(visit * 0.2)

        return visit

if __name__ == "__main__":
    if len(sys.argv) > 1:
        year, month, day = [int(v) for v in sys.argv[1].split("-")]
    else:
        year, month, day = 2025, 8, 15
    queried_date = date(year, month, day)

    sensor = sensor_visit(1200, 300)

    # Test de notre fonction de malfunction et casse du sensor
    init_date = date(2025, 7, 1)
    while init_date < date(2025,8,25):
        init_date += timedelta(days=1)
        visit_count = sensor.get_visit_count(init_date)
        print(init_date, visit_count)