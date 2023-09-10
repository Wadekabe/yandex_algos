class Graph():
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.graph = []
        self.visited_vertices = [False for i in range(vertices + 1)]
        self.graph_comp = [0 for i in range(vertices + 1)]

    def graph_reading(self):
        self.graph = [[] for i in range(self.vertices + 1)]
        for edge in range(self.edges):
            vert1, vert2 = map(int, input().split())
            if vert1 != vert2:
                self.graph[vert1].append(vert2)
                self.graph[vert2].append(vert1)
            else:
                self.graph[vert1].append(vert2)

    def graph_reading_from_file(self, file="input.txt"):
        with open(file) as f:
            self.vertices, self.edges = map(int, f.readline().split())
            self.graph = [[] for i in range(self.vertices + 1)]
            self.visited_vertices = [False for i in range(self.vertices + 1)]
            self.graph_comp = [0 for i in range(self.vertices + 1)]
            for edges in f:
                vert1, vert2 = map(int, edges.split())
                if vert1 != vert2:
                    self.graph[vert1].append(vert2)
                    self.graph[vert2].append(vert1)
                else:
                    self.graph[vert1].append(vert2)

    def dfs(self, now, conn_comp_num):
        self.visited_vertices[now] = True
        self.graph_comp[now] = conn_comp_num
        for neig in self.graph[now]:
            if not self.visited_vertices[neig]:
                self.dfs(neig, conn_comp_num)

    def connect_comp_define(self):
        comp_num = 1
        for i in range(1, self.vertices + 1):
            if not self.visited_vertices[i]:
                self.dfs(i, comp_num)
                comp_num += 1

    def show_info(self):
        print(self.graph, "\n", self.visited_vertices, "\n", self.graph_comp)

    def connect_comp(self, vertice):
        num_elem = 0
        elems = []
        comp_num = self.graph_comp[vertice]
        for vert in range(1, self.vertices+1):
            if self.graph_comp[vert] == comp_num:
                num_elem += 1
                elems.append(vert)
        return num_elem, elems
