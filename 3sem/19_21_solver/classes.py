class GameModel:
    def __init__(self, heaps, win_type, target, moves):
        self.heaps = heaps
        self.win_type = win_type
        self.target = target
        self.moves = moves
        self.memo = {}

    def check_win(self, h1, h2):
        s = h1 + h2
        if self.win_type == ">=":
            return s >= self.target
        return s <= self.target

    def make_moves(self, h1, h2):
        res = []
        for m in self.moves:
            try:
                n1 = int(eval(m, {}, {'x': h1}))
                if n1 > 0:
                    res.append((n1, h2))
            except: pass

        if self.heaps == 2:
            for m in self.moves:
                try:
                    n2 = int(eval(m, {}, {'x': h2}))
                    if n2 > 0:
                        res.append((h1, n2))
                except: pass
        return sorted(list(set(res)))

    def solve(self, h1, h2, depth):
        key = (h1, h2, depth)
        if key in self.memo: return self.memo[key]
        if self.check_win(h1, h2): return 0
        if depth == 0: return 0

        next_pos = self.make_moves(h1, h2)
        if not next_pos: return 0

        res = [self.solve(n1, n2, depth - 1) for n1, n2 in next_pos]

        if any(self.check_win(n1, n2) for n1, n2 in next_pos):
            self.memo[key] = 1
            return 1

        if all(r == 1 for r in res):
            self.memo[key] = 2
            return 2

        if any(r == 2 for r in res):
            self.memo[key] = 3
            return 3

        if all(r == 1 or r == 3 for r in res):
            self.memo[key] = 4
            return 4

        self.memo[key] = 0
        return 0

    def check_mistake(self, h1, h2):
        next_pos = self.make_moves(h1, h2)
        for n1, n2 in next_pos:
            if not self.check_win(n1, n2):
                if self.solve(n1, n2, 1) == 1:
                    return True
        return False

    def get_data(self, fixed, s_min, s_max):
        data = {
            "19_mistake": [],
            "19_win1": [],
            "20": [],
            "21": []
        }
        self.memo = {}

        for s in range(s_min, s_max + 1):
            if self.heaps == 1:
                h1, h2 = s, 0
            else:
                h1, h2 = fixed, s

            if self.check_win(h1, h2): continue

            code = self.solve(h1, h2, 4)

            if code == 1: data["19_win1"].append(s)
            if code == 3: data["20"].append(s)
            if code == 4: data["21"].append(s)

            if self.check_mistake(h1, h2):
                data["19_mistake"].append(s)

        return data