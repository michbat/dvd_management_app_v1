'''
Classe DVD - Modèle de données pour représenter un DVD dans l'application.
Cette classe encapsule les informations d'un DVD (titre, réalisateur, année)
avec validation des données et contrôle d'accès via des propriétés.
'''


class DVD:
    def __init__(self, id: int, titre: str, realisateur: str, annee: int) -> None:
        '''
        Initialise une nouvelle instance de DVD avec les informations fournies.
        Tous les attributs sont encapsulés (privés) pour contrôler l'accès
        via les propriétés de la classe
        '''
        self.__id = id
        self.__titre = titre
        self.__realisateur = realisateur
        self.__annee = annee

    @property
    def id(self) -> int:
        '''
        Retourne l'identifiant unique du DVD. Cet attribut est en lecture seule
        car il ne doit pas être modifié après la création de l'objet
        '''
        return self.__id

    @property
    def titre(self) -> str:
        '''
        Retourne le titre du DVD
        '''
        return self.__titre

    @titre.setter
    def titre(self, value: str) -> None:
        '''
        Modifie le titre du DVD après validation. Le titre doit être une chaîne
        de caractères non vide et ne contenir que des espaces
        '''
        if isinstance(value, str) and value.strip():
            self.__titre = value
        else:
            raise ValueError("La valeur doit être une chaîne non vide")

    @property
    def realisateur(self) -> str:
        '''
        Retourne le nom du réalisateur du DVD
        '''
        return self.__realisateur

    @realisateur.setter
    def realisateur(self, value: str) -> None:
        '''
        Modifie le nom du réalisateur après validation. Le nom doit être une
        chaîne de caractères non vide et ne contenir que des espaces
        '''
        if isinstance(value, str) and value.strip():
            self.__realisateur = value
        else:
            raise ValueError("La valeur doit être une chaîne non vide")

    @property
    def annee(self) -> int:
        '''
        Retourne l'année de sortie du DVD
        '''
        return self.__annee

    @annee.setter
    def annee(self, value: int) -> None:
        '''
        Modifie l'année de sortie après validation. L'année doit être un entier
        compris entre 1930 et 2025 inclus
        '''
        if isinstance(value, int) and 1930 <= value <= 2025:
            self.__annee = value
        else:
            raise ValueError(
                "L'année doit être un entier compris entre 1930 et 2025")

    def __str__(self) -> str:
        '''
        Retourne une représentation textuelle formatée du DVD pour l'affichage.
        Inclut le titre, le réalisateur et l'année de sortie sur des lignes séparées
        '''
        return (f"Titre : {self.__titre}\n" +
                f"Réalisateur : {self.__realisateur}\n" +
                f"Année de sortie : {self.__annee}")
