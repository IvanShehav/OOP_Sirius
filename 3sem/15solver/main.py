import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
                               QWidget, QLabel, QLineEdit, QPushButton, QComboBox)
from classes import Reshatel, Holst

class Okno(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Решение 15 задания (Метод координат)")
        self.resize(850, 600)

        self.mozg = Reshatel()

        centr = QWidget()
        self.setCentralWidget(centr)
        maket = QVBoxLayout(centr)

        def sozd_pole(txt):
            box = QHBoxLayout()
            box.addWidget(QLabel(txt))
            e1 = QLineEdit()
            e2 = QLineEdit()
            box.addWidget(e1)
            box.addWidget(e2)
            maket.addLayout(box)
            return e1, e2

        self.ep1, self.ep2 = sozd_pole("P:")
        self.eq1, self.eq2 = sozd_pole("Q:")
        self.er1, self.er2 = sozd_pole("R:")

        hbox = QHBoxLayout()
        hbox.addWidget(QLabel("Формула:"))
        self.ef = QLineEdit()
        self.ef.setPlaceholderText("Вставьте формулу, например: ((x ∈ P) ≡ (x ∈ Q)) → ¬(x ∈ A)")
        hbox.addWidget(self.ef)
        maket.addLayout(hbox)

        self.cb = QComboBox()
        self.cb.addItems(["Максимальная длина", "Минимальная длина"])
        maket.addWidget(self.cb)

        btn = QPushButton("Найти решение")
        btn.clicked.connect(self.start)
        maket.addWidget(btn)

        self.lbl = QLabel("Готов к работе")
        self.lbl.setStyleSheet("font-size: 16px; color: yellow; font-weight: bold;")
        maket.addWidget(self.lbl)

        self.ris = Holst()
        maket.addWidget(self.ris)

    def start(self):
        self.ris.ochistit()
        self.lbl.setText("Вычисляю...")
        QApplication.processEvents()

        try:
            p = [int(self.ep1.text()), int(self.ep2.text())]
            q = [int(self.eq1.text()), int(self.eq2.text())]

            r = []
            if self.er1.text() and self.er2.text():
                r = [int(self.er1.text()), int(self.er2.text())]

            frm = self.ef.text()
            mode = "max" if "Макс" in self.cb.currentText() else "min"

            val, otr, ok = self.mozg.vychislit(p, q, r, mode, frm)

            if ok:
                self.lbl.setText(f"Ответ: {val}  |  Отрезок A: {otr}")
                self.ris.ustanovit_dannye(p, q, r, otr)
            else:
                self.lbl.setText("Решений нет")

        except Exception:
            self.lbl.setText("Ошибка в данных или формуле")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Okno()
    w.show()
    sys.exit(app.exec())