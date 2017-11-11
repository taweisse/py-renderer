import numpy

class Object:
    def __init__(self):
        self.name = str()
        self.verticies = list()
        self.edges = list()
        self.worldPos = [0,0,0]

    def loadModel(self, filename):
        file = open(filename, "r")

        for line in file:
            line.lstrip()
            if line[0] == "#":
                continue

            elif line[0] == "o":
                self.name = line.split()[1]
                continue

            elif line[0] == "v":
                tmp = [float(i) for i in line.split()[1:]]
                tmp.append(1)
                self.verticies.append(tmp)
                continue

            elif line[0] == "f":
                tmp = [int(i) for i in line.split()[1:]]
                if [tmp[0] - 1, tmp[1] - 1] not in self.edges and [tmp[1] - 1, tmp[0] - 1] not in self.edges:
                    self.edges.append([tmp[0] - 1, tmp[1] - 1])
                if [tmp[1] - 1, tmp[2] - 1] not in self.edges and [tmp[2] - 1, tmp[1] - 1] not in self.edges:
                    self.edges.append([tmp[1] - 1, tmp[2] - 1])
                if [tmp[2] - 1, tmp[0] - 1] not in self.edges and [tmp[0] - 1, tmp[2] - 1] not in self.edges:
                    self.edges.append([tmp[2] - 1, tmp[0] - 1])
                
        file.close()