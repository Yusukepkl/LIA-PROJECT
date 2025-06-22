"""Inicializa a aplicacao Lia"""

from lia.interface.app import run
from lia.database.db import init_db


def main():
    init_db()
    run()


if __name__ == '__main__':
    main()
