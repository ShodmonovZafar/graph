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
    
    def __init__(self, name: str, head = None, end = None) -> None:
        self.name = name
        self.head = head
        self.end = end
    
    def get_name(self):
        return self.name
    
    def set_name(self, name: str) -> None:
        self.name = name
        
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
    def __init__(self, data: str) -> None:
        self.data = data
        self.edges = []
    
    def get_data(self):
        return self.data
    
    def set_data(self, data: str) -> None:
        self.data = data
        
    def get_edges(self):
        return self.edges
    
    def set_edges(self, edge):
        self.edges.append(edge)

    def __str__(self) -> str:
        return self.data

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
        
    
    
    
node_a = Node("A")
node_b = Node("B")
node_c = Node("C")

edge_a_a = Edge("a_a", node_a, node_a)
edge_a_b = Edge("a_b", node_a, node_b)
edge_a_c = Edge("a_c", node_a, node_c)
edge_b_c = Edge("b_c", node_b, node_c)
edge_c_b = Edge("c_b", node_c, node_b)


# print(edge_a_a.head.data)
# print(edge_a_a.end.data)
# print(edge_a_b.head.data)
# print(edge_a_b.end.data)

node_a.set_edges(edge_a_a)
node_a.set_edges(edge_a_b)
node_a.set_edges(edge_a_c)
for i in node_a.get_edges():
    print(i)

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