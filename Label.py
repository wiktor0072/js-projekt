from PySide6.QtWidgets import QLabel


class MyLabel(QLabel):

    def __init__(self, parent):
        super().__init__(parent)

    def set_original_mouse_events(self):
        self.mousePressEvent = QLabel().mousePressEvent
        self.mouseMoveEvent = QLabel().mouseMoveEvent
        self.mouseReleaseEvent = QLabel().mouseReleaseEvent
        self.mousePaintEvent = None