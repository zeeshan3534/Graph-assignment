class Graph(object):
    def __init__(self):
        self.vertexs = ['NUST Islamabad','UIT Karachi','UET Lahore','BZU Multan','Faisalabad Uni']

    def build_graph(self):
        ver1 = 'NUST Islamabad'
        ver2 = 'UIT Karachi'
        ver3 = 'UET Lahore'
        ver4 = 'BZU Multan'
        ver5 = 'Faisalabad Uni'
        g = {ver1:[ver2,ver4],ver2:[ver3],ver3:[ver2,ver4,ver5],ver4:[ver5,ver3,ver1],ver5:[ver4,ver3]}
        return g

class SharedData(object):
    def __init__(self):
        self.graph = Graph()
        self.path=[]



    def minimum_cost_path(self,graph, start, end, path=[]):
        path = path + [start]

        if start == end:

            return path

        if start not in self.graph.vertexs:
            return "Wrong vertexs"
        for neigh in self.graph.build_graph()[start]:
            if neigh not in path:
                path1 = self.minimum_cost_path(graph, neigh, end, path)
                if path1:
                    for i in path1:
                        self.path.append(i)
                    return path1



    def calculate_cost(self, mincostpath):
        try:
            pathcost=0
            while pathcost<len(mincostpath)-1:
                pathcost+=1
            return f"The Cost is {pathcost}"
        except:
            return "wronge Path"
data = SharedData()
graph = Graph()

shortest_path = data.minimum_cost_path(graph,"UIT Karachi","NUST Islamabad")
print(shortest_path)
print(data.calculate_cost(shortest_path))
