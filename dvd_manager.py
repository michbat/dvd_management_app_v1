'''
Classe DVDManager qui gère le CRUD des DVD dans la base de données SQLite
'''

from dvd import DVD
import os
import sqlite3


class DVDManager:
    def __init__(self) -> None:
        # Connexion à la BDD lors de la création d'un objet DVDManager
        with DVDManager.db_connexion() as connexion:
            self.__cursor: sqlite3.Cursor = connexion.cursor()

    # Getter pour l'attribut __cursor
    @property
    def cursor(self) -> sqlite3.Cursor:
        return self.__cursor

    # Methode utilitaire pour la connexion à la BDD

    @classmethod
    def db_connexion(cls):
        '''
        La méthode de classe db_connexion() crée et retourne une connexion à la base de
        données
        '''
        db_path: str = os.path.join(
            os.path.dirname(__file__), "collection.db")
        connexion = None
        try:
            connexion = sqlite3.connect(db_path)
            connexion.row_factory = sqlite3.Row
            print("Connexion à la base de données ...\n")
            return connexion

        except sqlite3.Error as e:
            print(f"Erreur lors de la connexion à la table : {e}")
            raise

    # Méthode d'instance get_all_dvds()
    def recuperer_dvd(self) -> list[DVD]:
        request: str = "SELECT * FROM dvd ORDER BY annee ASC"

        self.cursor.execute(request)
        results = self.cursor.fetchall()

        # Convertir les sqlite3.Row en objets DVD
        dvd_objects: list[DVD] = []
        for row in results:
            dvd = DVD(row['id'], row['titre'],
                      row['realisateur'], row['annee'])
            dvd_objects.append(dvd)

        # On retourne les objets DVD
        return dvd_objects

    # Méthode d'instance create_table()
    def create_table(self) -> str:
        request: str = '''
        CREATE TABLE IF NOT EXISTS dvd(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            titre VARCHAR(250) NOT NULL,
            realisateur VARCHAR(250) NOT NULL,
            annee INTEGER NOT NULL CHECK (annee >= 1930 AND annee <= 2025)
        )
        '''
        self.cursor.execute(request)

        return "Table créée ou déjà existante."

    # Méthode d'instance ajouter_dvd(dvd)
    def ajouter_dvd(self, dvd: tuple):

        self.cursor.execute(
            "INSERT INTO dvd (titre,realisateur,annee) VALUES (?,?,?)", dvd
        )
        self.cursor.connection.commit()

    # Méthode d'instance supprimer_dvd(id)

    @classmethod
    def get_dvd_to_insert(cls) -> tuple[str, str, int]:
        print(f"\n{'*' * 10} AJOUT D'UN DVD {'*' * 10}\n")
        titre: str = input("Titre du film : ")
        realisateur: str = input("Le nom du réalisateur: ")

        while True:
            try:
                annee_str: str = input("Année de sortie: ")
                annee: int = int(annee_str)
                if not 1930 <= annee <= 2025:
                    raise AssertionError(
                        "L'année de sortie doit être comprise entre 1930 et 2025")
                # La méthode de classe utilitaire renvoit un tuple
                print("\nLe DVD a été rajouté!\n")
                return (titre, realisateur, annee)
            except ValueError:
                print("Vous devez saisir un entier SVP ")
            except AssertionError as e:
                print(e)
