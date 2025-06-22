from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
import os


def run():
    app = QApplication([])
    engine = QQmlApplicationEngine()
    qml_file = os.path.join(os.path.dirname(__file__), 'qml', 'MainView.qml')
    engine.load(qml_file)
    if not engine.rootObjects():
        raise RuntimeError('Falha ao carregar a interface QML')
    app.exec()


if __name__ == '__main__':
    run()
