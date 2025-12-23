from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QFont, QPen
from PySide6.QtCore import Qt

class Reshatel:
    def __init__(self):
        self.koord_p = []
        self.koord_q = []
        self.koord_r = []

    def podgotovit_tekst(self, tekst):
        t = tekst.replace(" ", "")

        sl = {
            "∈": "in",
            "->": "<=",
            "→": "<=",
            "≡": "==",
            "¬": "not",
            "∧": "and",
            "∨": "or",
            "&": "and",
            "|": "or",
            "~": "not",
            "х": "x",
            "Х": "x",
            "Р": "P",
            "А": "A",
            "В": "B",
            "С": "C",
        }

        for k, v in sl.items():
            t = t.replace(k, v)

        t = t.replace("xinP", "P")
        t = t.replace("xinQ", "Q")
        t = t.replace("xinR", "R")
        t = t.replace("xinA", "A")
        t = t.replace("x in P", "P")

        return t

    def proverit_x(self, x, p, q, r, a, formula):
        P = (p[0] <= x <= p[1])
        Q = (q[0] <= x <= q[1])
        R = False
        if r:
            R = (r[0] <= x <= r[1])
        A = (a[0] <= x <= a[1])

        kontekst = {"x": x, "P": P, "Q": Q, "R": R, "A": A}
        return eval(formula, {}, kontekst)

    def vychislit(self, p, q, r, rezhim, formula_siraya):
        self.koord_p = p
        self.koord_q = q
        self.koord_r = r

        vse_tochki = set(p + q)
        if r:
            vse_tochki.update(r)

        spisok_tochek = sorted(list(vse_tochki))

        tochki_testa = sorted(list(vse_tochki))

        formula = self.podgotovit_tekst(formula_siraya)

        luchshiy_rez = 0 if rezhim == "max" else 10**9
        luchshiy_otr = []
        nashlos = False

        min_scan = min(spisok_tochek) - 2
        max_scan = max(spisok_tochek) + 2

        for i in range(len(spisok_tochek)):
            for j in range(i, len(spisok_tochek)):
                start_a = spisok_tochek[i]
                end_a = spisok_tochek[j]
                dlina = end_a - start_a

                otrezok_a = [start_a, end_a]

                podhodit = True

                for k in range(min_scan * 2, max_scan * 2 + 1):
                    x = k / 2.0
                    if not self.proverit_x(x, p, q, r, otrezok_a, formula):
                        podhodit = False
                        break

                if podhodit:
                    nashlos = True
                    if rezhim == "max":
                        if dlina > luchshiy_rez:
                            luchshiy_rez = dlina
                            luchshiy_otr = otrezok_a
                    else:
                        if dlina < luchshiy_rez:
                            luchshiy_rez = dlina
                            luchshiy_otr = otrezok_a

        return luchshiy_rez, luchshiy_otr, nashlos

class Holst(QWidget):
    def __init__(self):
        super().__init__()
        self.data_p = []
        self.data_q = []
        self.data_r = []
        self.data_a = []
        self.setMinimumHeight(250)

    def ochistit(self):
        self.data_p = []
        self.data_q = []
        self.data_r = []
        self.data_a = []
        self.update()

    def ustanovit_dannye(self, p, q, r, a):
        self.data_p = p
        self.data_q = q
        self.data_r = r
        self.data_a = a
        self.update()

    def paintEvent(self, event):
        p = QPainter(self)
        w = self.width()
        h = self.height()

        p.setBrush(QColor(30, 30, 30))
        p.drawRect(0, 0, w, h)

        if not self.data_p and not self.data_q:
            return

        points = self.data_p + self.data_q + self.data_r + self.data_a
        if not points: return

        mn = min(points)
        mx = max(points)
        rng = mx - mn
        if rng == 0: rng = 1

        pad = 40
        scale = (w - 2 * pad) / (rng + 4)

        def gx(val):
            return pad + (val - mn + 2) * scale

        p.setFont(QFont("Arial", 10))

        def draw_seg(y, d, col, name):
            if not d: return
            x1 = gx(d[0])
            x2 = gx(d[1])
            p.setBrush(col)
            p.setPen(Qt.NoPen)
            p.drawRect(x1, y, x2 - x1, 20)
            p.setPen(QColor(255, 255, 255))
            p.drawText(10, y + 15, name)
            p.drawText(x1, y - 5, str(d[0]))
            p.drawText(x2, y - 5, str(d[1]))

        draw_seg(40, self.data_p, QColor(70, 130, 180), "P")
        draw_seg(90, self.data_q, QColor(205, 92, 92), "Q")

        ny = 140
        if self.data_r:
            draw_seg(140, self.data_r, QColor(147, 112, 219), "R")
            ny = 190

        draw_seg(ny, self.data_a, QColor(50, 205, 50), "A")