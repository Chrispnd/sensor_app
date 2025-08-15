from fake_data.store import store_sensor

def create_app() -> dict:
    """
    Créer les magasins pour que notre API fonctionne;
    5 magasins avec chacun 8 capteurs
    """

    store_name = ["Lille", "Paris", "Lyon", "Toulouse", "Marseille"]
    store_avg_visit = [3000, 8000, 6000, 2000, 1350]
    store_std_visit = [500, 800, 500, 300, 50]
    perc_malfunction = [0.05, 0.1, 0.06, 0.14, 0.02]
    perc_break = [0.01, 0.04, 0.07, 0.12, 0.04]

    store_dict = dict()

    for i in range(len(store_name)):
        store_dict[store_name[i]] = store_sensor(
            store_name[i]
            , store_avg_visit[i]
            , store_std_visit[i]
            , perc_malfunction[i]
            , perc_break[i]
        )

    return store_dict