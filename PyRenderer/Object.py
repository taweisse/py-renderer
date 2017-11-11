import numpy

class Object:
    def __init__(self):
        self.name = str()
        self.verticies = list()

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
                tmp = ([float(i) for i in line.split()[1:]])
                tmp.append(1)
                self.verticies.append(tmp)
                continue

        file.close()