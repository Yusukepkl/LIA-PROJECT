from PySide6.QtGui import QVector3D
from PySide6.QtCore import QObject

class ModelController(QObject):
    """Controlador simples para aplicar blend shapes."""

    def __init__(self, model):
        super().__init__()
        self.model = model
        self.blend_shapes = {}

    def set_blend_shape(self, name: str, value: float):
        if name in self.blend_shapes:
            self.blend_shapes[name] = value
            # Aqui seria aplicada a transformação no modelo

    def look_at(self, x: float, y: float):
        # Girar o rosto em direção ao ponto (x, y)
        self.model.setProperty('lookX', x)
        self.model.setProperty('lookY', y)
