import networkx as nx
import matplotlib.pyplot as plt
import random

'''
1 <= p <= 100 nombre de sommet dans cahcun des sous complexes (t sous complexe)
t entier nombre de sous complexe
'''
def generateGraph(p: int, t: int):
    vertices = [ i for i in range(0, 100)]

    def getRandomVertex():
        return vertices[random.randint(0, len(vertices) - 1)]
    
    sets = []

    for _ in range(0, t):
        s = set()
        while len(s) != p:
            s.add(getRandomVertex())
        
        sets.append(s)
    return sets


def applyAlgo1(sets, delta):
    g = nx.Graph()
    for s in sets:
        last_vertex = None
        for vertex in s:
            if not g.has_node(vertex):
                g.add_node(vertex)
                
            if last_vertex != None:
                g.add_edge(vertex, last_vertex)
            last_vertex = vertex
        for node in g.nodes():
            if g.degree(node) > delta:
                return False

    return True
    

s1 = set([1,2,3])
s2 = set([1,6,7])
s3 = set([2,4,5])
s4 = set([4,5,6])
s5 = set([7,8,9,10])

sets  = [s1, s2, s3, s4, s5]

s21 = set([1,2,3])
s22 = set([2,4,5])
s23 = set([3,4,5])
s24 = set([4,5,6,7])

sets2 = [s21, s22, s23,s24]

graph = applyAlgo1(sets2, 3)

print(graph)
#nx.draw(graph, with_labels=True)
#plt.show()

