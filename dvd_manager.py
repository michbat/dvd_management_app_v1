'''
Classe DVDManager qui gère le CRUD des DVD dans la base de données SQLite
'''

from dvd import DVD
import os
import sqlite3


class DVDManager:
    def __init__(self) -> None:
        '''
        Initialise une nouvelle instance de DVDManager en établissant la connexion
        à la base de données SQLite et en créant un cursor pour les opérations
        '''
        self.__connexion = DVDManager.db_connexion()
        self.__cursor: sqlite3.Cursor = self.__connexion.cursor()

    @property
    def cursor(self) -> sqlite3.Cursor:
        '''
        Retourne le cursor SQLite pour l'exécution des requêtes sur la base de données
        '''
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

    def recuperer_dvd(self) -> list[DVD]:
        '''
        Récupère tous les DVDs de la base de données et les retourne sous forme
        d'une liste d'objets DVD triée par année croissante
        '''
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

    def recuperer_un_dvd(self, id: int) -> "DVD":
        '''
        Récupère un DVD de la base de données grâce à une ID et le retourne sous forme d'un objet
        DVD
        '''
        request: str = "SELECT * FROM dvd WHERE id = ?"
        self.cursor.execute(request, (id,))
        result = self.cursor.fetchone()
        dvd_object = DVD(result['id'], result['titre'],
                         result['realisateur'], result['annee'])

        return dvd_object

    def create_table(self) -> str:
        '''
        Crée la table dvd dans la base de données si elle n'existe pas déjà.
        La table contient les champs : id, titre, realisateur, et annee avec
        des contraintes de validation appropriées
        '''
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

    def ajouter_dvd(self, dvd: tuple) -> bool:
        '''
        Ajoute un nouveau DVD dans la base de données à partir d'un tuple contenant
        le titre, le réalisateur et l'année. Retourne True en cas de succès,
        False en cas d'échec
        '''
        try:
            self.cursor.execute(
                "INSERT INTO dvd (titre,realisateur,annee) VALUES (?,?,?)", dvd
            )
            self.cursor.connection.commit()

            # Vérifier si l'insertion a réussi
            if self.cursor.rowcount > 0:
                print(
                    f"\nDVD ajouté avec succès (ID: {self.cursor.lastrowid})\n")
                return True
            else:
                print("\nÉchec de l'ajout du DVD\n")
                return False

        except sqlite3.Error as e:
            print(f"\nErreur lors de l'ajout du DVD: {e}\n")
            return False

    def supprimer_dvd(self, id: int) -> bool:
        '''
        Supprime un DVD de la base de données en utilisant son identifiant unique.
        Retourne True si la suppression a réussi, False si aucun DVD n'a été trouvé
        ou en cas d'erreur
        '''
        try:
            request: str = "DELETE FROM dvd WHERE id = ?"
            self.cursor.execute(request, (id,))
            self.cursor.connection.commit()

            # Vérifier si la suppression a réussi
            if self.cursor.rowcount > 0:
                print(f"\nDVD avec ID {id} supprimé avec succès\n")
                return True
            else:
                print(f"\nAucun DVD trouvé avec l'ID {id}\n")
                return False

        except sqlite3.Error as e:
            print(f"\nErreur lors de la suppression du DVD: {e}\n")
            return False

    # Méthode pour fermer la connexion à la BDD
    def fermer_connexion(self):
        """Ferme la connexion à la base de données"""
        if hasattr(self, '_DVDManager__connexion') and self.__connexion:
            self.__connexion.close()
            print("Connexion à la base de données fermée.\n")

    @classmethod
    def get_dvd_to_insert(cls) -> tuple[str, str, int]:
        '''
        Méthode de classe qui collecte les informations d'un nouveau DVD auprès
        de l'utilisateur via une interface en ligne de commande. Valide l'année
        de sortie et retourne un tuple (titre, réalisateur, année)
        '''
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
                return (titre, realisateur, annee)
            except ValueError:
                print("Vous devez saisir un entier SVP ")
            except AssertionError as e:
                print(e)

    def __del__(self) -> None:
        '''
        Destructeur appelé automatiquement lors de la destruction de l'objet.
        S'assure que la connexion à la base de données est correctement fermée
        pour éviter les fuites de ressources
        '''
        self.fermer_connexion()
