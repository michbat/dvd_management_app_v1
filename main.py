'''


'''
from dvd import DVD
from dvd_manager import DVDManager


def main():
    dvd_manager: DVDManager = DVDManager()
    # message: str = dvd_manager.create_table()
    # print(message)
    # print()

    # Afficher la liste des DVD dans la BDD
    try:
        dvd_manager.dvd_list = dvd_manager.show_table()
        for item in dvd_manager.dvd_list:
            print(item)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
