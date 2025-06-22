from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QUrl
from pathlib import Path
from .model_loader import ModelController

class LiaWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lia")
        self.engine = QQmlApplicationEngine()
        self.controller = ModelController()
        self.engine.rootContext().setContextProperty("modelController", self.controller)
        qml_path = Path(__file__).with_name('view.qml')
        self.engine.load(QUrl.fromLocalFile(str(qml_path)))
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
