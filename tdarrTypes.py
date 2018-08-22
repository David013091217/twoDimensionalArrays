class unavailableCoordinate(Exception):
    pass

class cell:
    def __init__(self, cX, cY, cV):
        self.cX = cX
        self.cY = cY
        self.cV = cV

class tARR:
    def __init__(self, aW, aH, uArr):
        self.aW = aW
        self.aH = aH
        self.uArr = uArr
    def _setup(self):
        if self.uArr != []:
            self.uArr = []
        for j in range(0, self.aH): 
            self.uArr.append([])
            for i in range(0, self.aW):
                self.uArr[j].append(cell(i, j, ""))
    def _edit(self, eX, eY, eV):
        self.eX = eX
        self.eY = eY
        self.eV = eV
        if not eX < self.aW or not eY < self.aH:
            if not eX < self.w:
                raise unavailableCoordinate(eX)
            elif not eY < self.h:
                raise unavailableCoordinate(eY)
        else:
            self.uArr[eX][eY].cV = eV
    def _output(self):
        out = ""
        for j in range(0, self.aH):
            for i in range(0, self.aW):
                if (type(self.uArr[i][j].cV) != "str"):
                    out += str(self.uArr[i][j].cV)+' '
                else:
                    out += self.uArr[i][j].cV+' '
            print(out)
            out = ""
