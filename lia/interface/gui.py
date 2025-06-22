from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtQml import QQmlApplicationEngine
from pathlib import Path

class LiaWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lia")
        self.engine = QQmlApplicationEngine()
        qml_path = Path(__file__).with_name('view.qml')
        self.engine.load(str(qml_path))
        if not self.engine.rootObjects():
            raise RuntimeError("Erro ao carregar a interface QML")

    def show(self):
        super().show()
        for obj in self.engine.rootObjects():
            obj.setParent(self)


def run():
    app = QApplication([])
    window = LiaWindow()
    window.show()
    app.exec()
