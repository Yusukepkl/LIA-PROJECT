from PySide6.QtGui import QVector3D
from PySide6.QtCore import QObject, Slot

class ModelController(QObject):
    """Controlador simples para aplicar blend shapes."""

    def __init__(self, model=None):
        super().__init__()
        self.model = model
        self.blend_shapes = {}

    @Slot(QObject)
    def set_model(self, model):
        self.model = model

    def set_blend_shape(self, name: str, value: float):
        if name in self.blend_shapes:
            self.blend_shapes[name] = value
            # Aqui seria aplicada a transformação no modelo

    @Slot(float, float)
    def look_at(self, x: float, y: float):
        """Gira o rosto em direção ao ponto normalizado (x, y)."""
        if not self.model:
            return
        yaw = (x - 0.5) * 30
        pitch = (y - 0.5) * -30
        self.model.setProperty('eulerRotation', QVector3D(pitch, yaw, 0))
