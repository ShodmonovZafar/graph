"""
The pseudo-code to create the matrix:

Procedure AdjacencyMatrix(N):    //N represents the number of nodes
Matrix[N][N]
for i from 1 to N
    for j from 1 to N
        Take input -> Matrix[i][j]
    endfor
endfor
"""

class Edge:
    
    def __init__(self, name: str, id = None, status = False, head = None, end = None) -> None:
        self.name = name
        self.id = id
        self.status = status
        self.head = head
        self.end = end
    
    def get_name(self):
        return self.name
    
    def set_name(self, name: str) -> None:
        self.name = name
        
    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id
    
    def get_status(self):
        return self.status
    
    def set_status(self, status):
        self.status = status
        
    def get_head(self):
        return self.head
    
    def set_head(self, head):
        self.head = head
    
    def get_end(self):
        return self.end
    
    def set_end(self, end):
        self.end = end
    
    def __str__(self) -> str:
        return self.name


class Node:
    def __init__(self, name: str, id) -> None:
        self.name = name
        self.id = id
        self.edges = []
    
    def get_name(self):
        return self.name
    
    def set_name(self, name: str) -> None:
        self.name = name
        
    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id
        
    def get_edges(self):
        return self.edges
    
    def set_edges(self, edge):
        self.edges.append(edge)

    def __str__(self) -> str:
        return self.name

class Graph_:
    
    def __init__(self, graph_name: str, number_of_nodes: int):
        self.__graph_name = graph_name
        self.__number_of_nodes = number_of_nodes
        
        
        self.__matrix = self.matrix_()
        self.__nodes_name = self.nodes_name_()
    
    def get_graph_name(self):
        return self.__graph_name
    
    def set_graph_name(self, new_graph_name: str) -> None:
        self.__graph_name = new_graph_name
      
    def get_number_of_nodes(self) -> int:
        return self.__number_of_nodes
      
    def matrix_(self):
        matrix = []
        for i in range(self.__number_of_nodes):
            matrix.append([])
            for j in range(self.__number_of_nodes):
                matrix[i].append(None)
        return matrix
    
    def nodes_name_(self) -> dict[str]:
        name_nodes = {}
        for i in range(self.__number_of_nodes):
            name_nodes[i] = None
        return name_nodes
    
    def get_nodes_name(self):
        return self.__nodes_name
    
    def set_nodes_name(self, nodes_name : list[str]) -> None:
        for i, e in enumerate(nodes_name):
            self.__nodes_name[i] = e

    def get_matrix(self):
        return self.__matrix
    
    def set_matrix(self):
        """n represents the number of nodes"""
        for i in range(self.__number_of_nodes):
            for j in range(self.__number_of_nodes):
                self.__matrix[i][j] = input("({}, {}) elementni kiriting: ".format(self.__nodes_name[i], self.__nodes_name[j]))
        return self.__matrix
    

class Graph:
    
    def __init__(self, name: str, number_nodes: int) -> None:
        self.name = name
        self.number_nodes = number_nodes
        
        self.nodes = []
        self.new_nodes()
        
        self.edges = []
        self.new_edges()
        
    def get_name(self):
        return self.name
    
    def set_name(self, name: str):
        self.name = name
        
    def get_number_nodes(self):
        return self.number_nodes
        
    def set_number_nodes(self, number_nodes: int):
        self.number_nodes = number_nodes
    
    def new_nodes(self):
        # self.nodes = []
        for i in range(self.number_nodes):
            new_node = Node("{}-node".format(i), i)
            self.nodes.append(new_node)
            
    def new_edges(self):
        for i in range(self.number_nodes):
            for j in range(self.number_nodes):
                new_edge = Edge("({}, {})-edge".format(i, j), (i, j), self.nodes[i], self.nodes[j])
                self.edges.append(new_edge)
    
    def activation_edges(self):
        for i in self.edges:
            a = int(input("{}-ni bor yoki yo'qligini kiriting, bor bo'lsa 1, yo'q bo'ls 0 kiriting: ".format(i)))
            if a == 1:
                b = True
            else:
                b = False
            i.set_status(b)
    
    def search_edge_id(self, id: tuple):
        for i in self.edges:
            if i.get_id() == id:
                return i
    
    def activation_edge(self, id: tuple):
        edge = self.search_edge_id(id)
        edge.set_status(True)
            
            
    
    def set_name_nodes(self):
        pass
  
    def new_matrix(self):
        pass
        
    
    

graph_B = Graph("Graph B", 2)
graph_B.activation_edges()
for i in graph_B.edges:
    print(i, i.get_status())
    
graph_B.activation_edge((1, 1))
for i in graph_B.edges:
    print(i, i.get_status())

# node_a = Node("A")
# node_b = Node("B")
# node_c = Node("C")

# edge_a_a = Edge("a_a", node_a, node_a)
# edge_a_b = Edge("a_b", node_a, node_b)
# edge_a_c = Edge("a_c", node_a, node_c)
# edge_b_c = Edge("b_c", node_b, node_c)
# edge_c_b = Edge("c_b", node_c, node_b)


# print(edge_a_a.head.data)
# print(edge_a_a.end.data)
# print(edge_a_b.head.data)
# print(edge_a_b.end.data)

# node_a.set_edges(edge_a_a)
# node_a.set_edges(edge_a_b)
# node_a.set_edges(edge_a_c)
# for i in node_a.get_edges():
#     print(i)

# graph_A = Graph("Graph A", 3)
# print(graph_A.get_graph_name())
# print(graph_A.get_number_of_nodes())
# print(graph_A.get_nodes_name())
# print(graph_A.get_matrix())

# graph_A.set_graph_name("Graph Zafar")
# graph_A.set_nodes_name(["A", "B", "C"])
# graph_A.set_matrix()
# print(graph_A.get_graph_name())
# print(graph_A.get_number_of_nodes())
# print(graph_A.get_nodes_name())
# print(graph_A.get_matrix())