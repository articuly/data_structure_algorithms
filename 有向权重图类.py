# coding:utf-8
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected = {}

    def add_neighbor(self, nbr, weight=0):
        self.connected[nbr] = weight

    def __str__(self):
        return str(self.id) + 'connect to:' + str([x.id for x in self.connected])

    def get_connections(self):
        return self.connected.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected[nbr]


class Graph:
    def __init__(self):
        self.vert_list = {}
        self.size = 0

    def add_vertex(self, key):
        self.size += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, key):
        if key in self.vert_list:
            return self.vert_list[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.vert_list

    def add_edge(self, f, t, weight=0):
        if f not in self.vert_list:
            new_vertex = self.add_vertex(f)
        if t not in self.vert_list:
            new_vertex = self.add_vertex(t)
        self.vert_list[f].add_neighbor(self.vert_list[t], weight)

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())


if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.add_vertex(i)
    print(g.vert_list)
    g.add_edge(0, 1, 5)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 4)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 3)
    g.add_edge(4, 0, 1)
    g.add_edge(5, 4, 8)
    g.add_edge(5, 2, 1)
    for v in g:
        for w in v.get_connections():
            print('{}, {}'.format(v.get_id(), w.get_id()))
