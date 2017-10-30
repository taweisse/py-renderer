class Object:
    def __init__(self):
        self.name = str()
        self.verticies = list()

    def test(self):
        print("working!")

    def loadModel(self, filename):
        file = open(filename, "r")
        for line in file:
            line.lstrip()
            if line[0] == "#":
                continue
            elif line[0] == "o":
                self.name = line.split()[1]
                continue;
            elif line[0] == "v":
                self.verticies.append([float(i) for i in line.split()[1:]])
                continue;

        file.close()