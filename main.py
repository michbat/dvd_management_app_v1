'''


'''
from dvd import DVD
from dvd_manager import DVDManager


def afficher_dvd(dvds: list[DVD]) -> None:
    if not dvds:
        print("Aucun DVD trouvé dans la collection.")
        return

    print(f"Collection de DVDs ({len(dvds)} film(s) trouvé(s)):")
    print(f"{'=' * 41}\n")

    for i, dvd in enumerate(dvds, 1):
        print(f"DVD #{i}\n")
        print(dvd)
        if i < len(dvds):  # Pas de séparateur après le dernier
            print(f"\n{'-' * 30}\n")

    print(f"{'=' * 41}\n")


def main():
    dvd_manager: DVDManager = DVDManager()
    # message: str = dvd_manager.create_table()
    # print(message)

    # Récupérer les DVDs et les afficher
    # dvds: list[DVD] = dvd_manager.recuperer_dvd()
    # afficher_dvd(dvds)

    # Ajout d'un DVD et affichage après ajout

    # dvd_manager.ajouter_dvd(DVDManager.get_dvd_to_insert())
    # dvds = dvd_manager.recuperer_dvd()
    # afficher_dvd(dvds)

    # Suppression d'un DVD
    dvd_manager.supprimer_dvd(11)
    # dvds = dvd_manager.recuperer_dvd()
    # afficher_dvd(dvds)


if __name__ == "__main__":
    main()
