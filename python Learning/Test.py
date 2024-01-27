class Graph:
    def __init__(self):
        self.adj_list={}

    def print_graph(self):
        for vertex in self.adj_list:
            print(f'{vertex} : {self.adj_list[vertex]}')

    def add_vertex(self,vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex]=[]
            return True
        return False
    
    def add_edge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self,v1,v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    

    def remove_vertex(self,vertex):
        if vertex in self.adj_list.keys():
            for orther_vertex in self.adj_list[vertex]:
                self.adj_list[orther_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False






g=Graph()
g.add_vertex(1)
g.add_vertex(2)
g.print_graph()


g.add_edge(1,2)
g.print_graph()

# print('After Removing Edges')
# g.remove_edge(1,2)
# g.print_graph()

print('After Removing vrtex 1')
g.remove_vertex(1)
g.print_graph()