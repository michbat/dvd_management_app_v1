'''
Programme principal de gestion d'une collection de DVDs.
Offre une interface en ligne de commande pour afficher, ajouter et supprimer
des DVDs dans une base de données SQLite.
'''
from dvd import DVD
from dvd_manager import DVDManager
import os


def afficher_dvd(dvds: list[DVD]) -> None:
    '''
    Affiche une liste formatée de DVDs avec numérotation et séparateurs visuels.
    Si la liste est vide, affiche un message informatif
    '''
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

    print(f"\n{'=' * 41}\n")


def afficher_un_dvd(dvd: DVD) -> None:
    '''
    Affiche les détails d'un seul DVD avec un formatage spécial.
    Si le DVD n'existe pas, affiche un message d'erreur
    '''
    if not dvd:
        print("DVD pas trouvé")
        return
    print("DVD trouvé: ")
    print(f"{'=' * 11}\n")
    print(dvd)
    print(f"\n{'=' * 11}\n")


def get_menu() -> list[str]:
    '''
    Génère et retourne la liste des options du menu principal sous forme
    de chaînes de caractères formatées pour l'affichage
    '''
    menu_items: list[str] = [
        "1. Afficher la liste des DVD",
        "2. Ajouter un DVD",
        "3. Supprimer un DVD",
        "4. Quitter le programme",
    ]
    return menu_items


def get_dvd_id() -> int:
    '''
    Demande à l'utilisateur de saisir l'ID d'un DVD et valide que c'est un entier.
    Utilise la récursivité pour redemander en cas de saisie invalide
    '''
    id: int = 0
    try:
        id = int(input("\nID du DVD à supprimer : "))
        return id
    except ValueError:
        print("Entrez un nombre entier SVP !")
    return get_dvd_id() # Récursivité 


def main():
    '''
    Fonction principale qui gère la boucle d'interaction avec l'utilisateur.
    Affiche le menu, traite les choix et exécute les opérations correspondantes
    sur la collection de DVDs
    '''
    dvd_manager: DVDManager = DVDManager()
    choix: int = 0
    while True:
        print(f"\n{'=' * 10} MENU {'=' * 10}\n")
        for item in get_menu():
            print(item)
        choix_str: str = input("\nVotre choix (1,2,3 et 4) : ")
        try:
            choix = int(choix_str)
            if not 1 <= choix <= 4:
                raise AssertionError("\nChoisissez 1,2,3 ou 4 SVP!")

        except ValueError:
            print("\nEntrez un nombre entier SVP!")
            os.system("sleep 3")
            os.system("clear")
            continue
        except AssertionError as e:
            print(e)
            os.system("sleep 3")
            os.system("clear")
            continue

        match(choix):
            case 1:  # Afficher la liste des DVD
                os.system("clear")
                dvds: list[DVD] = dvd_manager.recuperer_dvd()
                afficher_dvd(dvds)
                os.system("sleep 10")
                os.system("clear")
            case 2:
                dvd_manager.ajouter_dvd(DVDManager.get_dvd_to_insert())
                os.system("sleep 2")
                os.system("clear")
            case 3:
                id: int = get_dvd_id()
                dvd_manager.supprimer_dvd(id)
                os.system("sleep 2")
                os.system("clear")

            case 4:
                print("\nAu revoir et à la prochaine!\n")
                os.system("sleep 1")
                os.system("clear")
                break


if __name__ == "__main__":
    main()
    os.system("sleep 1")
    os.system("clear")
