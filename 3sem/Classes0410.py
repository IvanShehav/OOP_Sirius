# classes.py
import itertools
import math
import networkx as nx

class GraphSolver:
    def __init__(self, matrix, target_graph_map):
        self.matrix = matrix
        self.target_graph_map = target_graph_map
        self.target_nodes = sorted(list(target_graph_map.keys()))
        self.num_nodes = len(self.target_nodes)
        self.solution_mapping = None

    def _is_mapping_valid(self, mapping):
        for node1 in self.target_nodes:
            for node2 in self.target_nodes:
                if node1 == node2:
                    continue
                p1_idx = mapping[node1]
                p2_idx = mapping[node2]
                # Защита от выхода индекса
                try:
                    has_connection_in_matrix = self.matrix[p1_idx][p2_idx] > 0
                except Exception:
                    return False
                has_connection_in_target_graph = node2 in self.target_graph_map.get(node1, [])
                if has_connection_in_target_graph != has_connection_in_matrix:
                    return False
        return True

    def solve(self):
        point_indices = list(range(self.num_nodes))
        for p_permutation in itertools.permutations(point_indices):
            current_mapping = {self.target_nodes[i]: p_permutation[i] for i in range(self.num_nodes)}
            if self._is_mapping_valid(current_mapping):
                self.solution_mapping = current_mapping
                return True
        return False

    def get_road_length(self, node1, node2):
        if not self.solution_mapping:
            return "Решение не найдено"
        p1_idx = self.solution_mapping.get(node1)
        p2_idx = self.solution_mapping.get(node2)
        if p1_idx is None or p2_idx is None:
            return "Неверные вершины"
        return self.matrix[p1_idx][p2_idx]


class GraphVisualizer:
    NODE_RADIUS = 24
    NODE_COLOR = "#ffcc00"

    def __init__(self, canvas, solution_mapping, matrix):
        self.canvas = canvas
        self.mapping = solution_mapping  # {'А': 0, 'Б': 1, ...}
        self.matrix = matrix
        self._positions = None

    def _calculate_positions(self):
        G = nx.Graph()
        nodes = list(self.mapping.keys())
        G.add_nodes_from(nodes)
        for i, node1 in enumerate(nodes):
            for node2 in nodes[i+1:]:
                p1_idx, p2_idx = self.mapping[node1], self.mapping[node2]
                try:
                    w = self.matrix[p1_idx][p2_idx]
                except Exception:
                    w = 0
                if w > 0:
                    G.add_edge(node1, node2, weight=w)
        pos = nx.spring_layout(G, seed=42, iterations=150)
        if not pos:
            # Если нет ребер, расположим по кругу
            n = len(nodes)
            pos = {}
            for idx, node in enumerate(nodes):
                angle = 2 * math.pi * idx / max(1, n)
                pos[node] = (math.cos(angle), math.sin(angle))
        self._positions = pos
        return pos

    def draw(self):
        self.canvas.delete("all")
        pos = self._calculate_positions()
        w = max(self.canvas.winfo_width(), 200)
        h = max(self.canvas.winfo_height(), 200)
        padding = self.NODE_RADIUS + 18

        coords = {}
        for node, (x, y) in pos.items():
            sx = padding + (x + 1) / 2 * (w - 2 * padding)
            sy = padding + (y + 1) / 2 * (h - 2 * padding)
            coords[node] = (sx, sy)

        # Рисуем ребра и подписи весов (смещённые перпендикулярно)
        for node1, p1_idx in self.mapping.items():
            for node2, p2_idx in self.mapping.items():
                if node1 >= node2:
                    continue
                try:
                    weight = self.matrix[p1_idx][p2_idx]
                except Exception:
                    weight = 0
                if weight > 0:
                    x1, y1 = coords[node1]
                    x2, y2 = coords[node2]
                    self.canvas.create_line(x1, y1, x2, y2, width=2)
                    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                    dx, dy = x2 - x1, y2 - y1
                    length = math.hypot(dx, dy) or 1.0
                    px, py = -dy / length, dx / length
                    offset = 12
                    tx, ty = mx + px * offset, my + py * offset
                    text_id = self.canvas.create_text(tx, ty, text=str(weight),
                                                      font=("Arial", 10, "bold"),
                                                      anchor="center", fill="blue")
                    bb = self.canvas.bbox(text_id)
                    if bb:
                        pad = 3
                        rect_id = self.canvas.create_rectangle(bb[0]-pad, bb[1]-pad, bb[2]+pad, bb[3]+pad,
                                                               fill="white", outline="")
                        self.canvas.lift(text_id)

        # Рисуем узлы
        for node, (x, y) in coords.items():
            self.canvas.create_oval(x - self.NODE_RADIUS, y - self.NODE_RADIUS,
                                     x + self.NODE_RADIUS, y + self.NODE_RADIUS,
                                     fill=self.NODE_COLOR, outline="black", width=2)
            self.canvas.create_text(x, y, text=node, font=("Arial", 12, "bold"))
