
class Gene:
    'Common base class for all employees'



    def __init__(self, *line):
        self.name = line[0][0]
        self.numOfExpressedCells = 0
        self.totalCalls = 0
        self. d = {}
        for i in range (1,len(line[0])):
            call = float(line[0][i])
            self.d[i] = call
            if call > 0:
                self.numOfExpressedCells += 1
                self.totalCalls += call











