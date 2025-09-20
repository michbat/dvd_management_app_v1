'''

Classe DVDManager qui gère une liste de DVD et le CRUD dans la base de données
'''

from dvd import DVD
import os
import sqlite3


class DVDManager:
    def __init__(self, dvd_list: list[DVD] = []) -> None:
        self.__dvd_list = dvd_list
        # Connexion à la BDD lors de la création d'un objet DVDManager
        with DVDManager.db_connexion() as connexion:
            self.__cursor: sqlite3.Cursor = connexion.cursor()

    # Getter et setter pour l'attribut __dvd_list

    @property
    def dvd_list(self) -> list[DVD]:
        return self.__dvd_list

    @dvd_list.setter
    def dvd_list(self, value: list[DVD]) -> None:
        if isinstance(value, list) and len(value) != 0 and all(isinstance(item, DVD) for item in value):
            self.__dvd_list = value
        else:
            raise ValueError("La liste doit être une liste non vide de DVD")

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

    # Méthode d'instance show_table()

    def show_table(self) -> list[DVD]:
        request: str = "SELECT * FROM dvd ORDER BY titre ASC"
        return self.cursor.execute(request).fetchall()

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


if __name__ == "__main__":
    dvdm = DVDManager()
