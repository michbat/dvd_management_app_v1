'''

La classe DVD qui sert de modèle à la base de données
'''


class DVD:
    def __init__(self, titre: str, realisateur: str, annee: int) -> None:
        self.__titre = titre
        self.__realisateur = realisateur
        self.__annee = annee

    # Getter et setter de l'attribue __titre
    @property
    def titre(self) -> str:
        return self.__titre

    @titre.setter
    def titre(self, value: str) -> None:
        if isinstance(value, str) and value.strip():
            self.__titre = value
        else:
            raise ValueError("La valeur doit être une chaîne non vide")

    # Getter et setter de l'attribut __realisateur
    @property
    def realisateur(self) -> str:
        return self.__realisateur

    @realisateur.setter
    def realisateur(self, value: str) -> None:
        if isinstance(value, str) and value.strip():
            self.__realisateur = value
        else:
            raise ValueError("La valeur doit être une chaîne non vide")

    # Getter et setter de l'attribut __annee
    @property
    def annee(self) -> int:
        return self.__annee

    @annee.setter
    def annee(self, value: int) -> None:
        if isinstance(value, int) and 1930 <= self.__annee <= 2025:
            self.__annee = value
        else:
            raise ValueError(
                "L'année doit être un entier compris entre 1930 et 2025")

    # Magic Methoc __str__

    def __str__(self) -> str:
        return (f"Titre : {self.__titre}\n" +
                f"Réalisateur : {self.__realisateur}\n" +
                f"Année de sortie : {self.__annee}")
