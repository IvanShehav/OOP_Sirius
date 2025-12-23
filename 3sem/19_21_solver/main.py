import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QLabel, QLineEdit, QRadioButton,
                               QButtonGroup, QComboBox, QPushButton, QGridLayout, QGroupBox)
from classes import GameModel

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ЕГЭ 19-21")
        self.resize(500, 500)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        # 1. Настройки игры
        group_game = QGroupBox("Параметры игры")
        grid = QGridLayout()

        self.rb1 = QRadioButton("1 Куча")
        self.rb2 = QRadioButton("2 Кучи")
        self.rb2.setChecked(True)
        bg = QButtonGroup(self)
        bg.addButton(self.rb1)
        bg.addButton(self.rb2)

        bg.buttonClicked.connect(self.change_mode)

        grid.addWidget(self.rb1, 0, 0)
        grid.addWidget(self.rb2, 0, 1)

        self.cb_cond = QComboBox()
        self.cb_cond.addItems([">= (Набрать)", "<= (Уменьшить)"])
        grid.addWidget(QLabel("Условие:"), 1, 0)
        grid.addWidget(self.cb_cond, 1, 1)

        self.in_target = QLineEdit("20")
        grid.addWidget(QLabel("Цель:"), 2, 0)
        grid.addWidget(self.in_target, 2, 1)

        self.lbl_fix = QLabel("1 куча (const):")
        self.in_fix = QLineEdit("10")
        grid.addWidget(self.lbl_fix, 3, 0)
        grid.addWidget(self.in_fix, 3, 1)

        grid.addWidget(QLabel("S (от и до):"), 4, 0)
        box_s = QHBoxLayout()
        self.s_min = QLineEdit("1")
        self.s_max = QLineEdit("100")
        box_s.addWidget(self.s_min)
        box_s.addWidget(self.s_max)
        grid.addLayout(box_s, 4, 1)

        group_game.setLayout(grid)
        main_layout.addWidget(group_game)

        # 2. Ходы
        group_moves = QGroupBox("Ходы (x - куча)")
        lay_moves = QHBoxLayout()
        self.m1 = QLineEdit("x-1")
        self.m2 = QLineEdit("(x+1)//2")
        self.m3 = QLineEdit("")
        lay_moves.addWidget(self.m1)
        lay_moves.addWidget(self.m2)
        lay_moves.addWidget(self.m3)
        group_moves.setLayout(lay_moves)
        main_layout.addWidget(group_moves)

        # 3. Настройка вопросов
        group_tasks = QGroupBox("Вопросы и Ответы")
        grid_t = QGridLayout()

        # 19 задание
        self.cb_19_type = QComboBox()
        self.cb_19_type.addItems(["Ваня (после ошибки)", "Петя (1 ход)"])
        self.cb_19_val = QComboBox()
        self.cb_19_val.addItems(["Максимальное", "Минимальное"])

        self.ans_19 = QLineEdit()
        self.ans_19.setReadOnly(True)

        grid_t.addWidget(QLabel("№19 Найти:"), 0, 0)
        grid_t.addWidget(self.cb_19_type, 0, 1)
        grid_t.addWidget(self.cb_19_val, 0, 2)
        grid_t.addWidget(self.ans_19, 0, 3)

        # 20 задание
        grid_t.addWidget(QLabel("№20 Петя (2 ход):"), 1, 0)
        grid_t.addWidget(QLabel("Вывод всех S"), 1, 1, 1, 2)
        self.ans_20 = QLineEdit()
        self.ans_20.setReadOnly(True)
        grid_t.addWidget(self.ans_20, 1, 3)

        # 21 задание
        self.cb_21_val = QComboBox()
        self.cb_21_val.addItems(["Максимальное", "Минимальное"])
        self.ans_21 = QLineEdit()
        self.ans_21.setReadOnly(True)

        grid_t.addWidget(QLabel("№21 Ваня (1-2 ход):"), 2, 0)
        grid_t.addWidget(self.cb_21_val, 2, 1, 1, 2)
        grid_t.addWidget(self.ans_21, 2, 3)

        group_tasks.setLayout(grid_t)
        main_layout.addWidget(group_tasks)

        # Кнопка
        btn = QPushButton("ПОЛУЧИТЬ ОТВЕТЫ")
        btn.setStyleSheet("font-weight: bold; font-size: 14px; padding: 10px;")
        btn.clicked.connect(self.calculate)
        main_layout.addWidget(btn)

    def change_mode(self):
        if self.rb1.isChecked():
            self.in_fix.setEnabled(False)
        else:
            self.in_fix.setEnabled(True)

    def calculate(self):
        try:
            h = 1 if self.rb1.isChecked() else 2
            wt = ">=" if ">=" in self.cb_cond.currentText() else "<="
            tgt = int(self.in_target.text())
            fix = int(self.in_fix.text()) if h == 2 else 0
            s1 = int(self.s_min.text())
            s2 = int(self.s_max.text())

            raw = [self.m1.text(), self.m2.text(), self.m3.text()]
            moves = [m for m in raw if m.strip()]

            game = GameModel(h, wt, tgt, moves)
            data = game.get_data(fix, s1, s2)

            # Ответ 19
            if self.cb_19_type.currentIndex() == 0:
                lst = data["19_mistake"]
            else:
                lst = data["19_win1"]

            if not lst:
                self.ans_19.setText("Нет")
            elif self.cb_19_val.currentIndex() == 0:
                self.ans_19.setText(str(max(lst)))
            else:
                self.ans_19.setText(str(min(lst)))

            # Ответ 20
            if data["20"]:
                self.ans_20.setText(str(data["20"]))
            else:
                self.ans_20.setText("Нет")

            # Ответ 21
            lst21 = data["21"]
            if not lst21:
                self.ans_21.setText("Нет")
            elif self.cb_21_val.currentIndex() == 0:
                self.ans_21.setText(str(max(lst21)))
            else:
                self.ans_21.setText(str(min(lst21)))

        except:
            self.ans_19.setText("Ошибка")
            self.ans_20.setText("ввода")
            self.ans_21.setText("данных")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = AppWindow()
    win.show()
    sys.exit(app.exec())