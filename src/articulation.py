class ArticulationPointFinder:
    def __init__(self, g):
        self.g = g
        self.n = len(g.adj)
        self.t = 0

        # Arrays for DFS properties
        self.disc = [-1] * self.n
        self.low = [-1] * self.n
        self.par = [-1] * self.n
        self.is_articulation_point = [False] * self.n

        self.find_points()

    def find_points(self):
        for v in range(self.n):
            if self.is_unvisited(v):
                self.dfs(v)

    def is_unvisited(self, v):
        return self.disc[v] < 0

    def init_vertex(self, u):
        self.disc[u] = self.low[u] = self.t
        self.t += 1

    def is_root_cut_vertex(self, u, children):
        return self.par[u] < 0 and children > 1

    def is_nonroot_cut_vertex(self, u, v):
        return self.par[u] >= 0 and self.low[v] >= self.disc[u]

    def update_low_time(self, u, v):
        self.low[u] = min(self.low[u], self.low[v])

    def update_back_edge(self, u, v):
        if v != self.par[u]:
            self.low[u] = min(self.low[u], self.disc[v])

    def dfs(self, u):
        children = 0
        self.init_vertex(u)

        for v in self.g.neighbors(u):
            if self.is_unvisited(v):
                self.par[v] = u
                children += 1
                self.dfs(v)
                self.update_low_time(u, v)

                if self.is_root_cut_vertex(u, children):
                    self.is_articulation_point[u] = True

                if self.is_nonroot_cut_vertex(u, v):
                    self.is_articulation_point[u] = True

            else:
                self.update_back_edge(u, v)
