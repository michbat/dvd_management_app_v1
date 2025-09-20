'''


'''
from dvd import DVD
from dvd_manager import DVDManager


def main():
    dvd_manager: DVDManager = DVDManager()
    message: str = dvd_manager.create_table()
    print(message)


if __name__ == "__main__":
    main()
