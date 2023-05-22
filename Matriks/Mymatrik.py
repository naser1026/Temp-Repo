class Matriks :
    from fractions import Fraction
    def __init__(self, name, matrik) :
        self.name = name
        self.matrik = matrik
        self.a11 = matrik[0][0]
        self.a12 = matrik[0][1]
        self.a13 = matrik[0][2]
        self.a21 = matrik[1][0]
        self.a22 = matrik[1][1]
        self.a23 = matrik[1][2]
        self.a31 = matrik[2][0]
        self.a32 = matrik[2][1]
        self.a33 = matrik[2][2]
        print(f"\nMatriks A = {self.matrik}")
        
    def determinan(self) :
        detmatrik = ((self.a11 * self.a22 * self.a33) + (self.a12 * self.a23 * self.a31) + (self.a13 * self.a21 * self.a32)) - ((self.a12 * self.a21 * self.a33) + (self.a11 * self.a23 * self.a32) + (self.a13 * self.a22 * self.a31))
        print(f"\nDeterminan dari matriks {self.name} = {detmatrik}")
        return detmatrik
        
    def adjoin (self) :
        m11 = [[self.a22, self.a23],[self.a32, self.a33]]
        m12 = [[self.a21, self.a23],[self.a31, self.a33]]
        m13 = [[self.a21, self.a22],[self.a31, self.a32]]
        m21 = [[self.a12, self.a13],[self.a32, self.a33]]
        m22 = [[self.a11, self.a13],[self.a31, self.a33]]
        m23 = [[self.a11, self.a12],[self.a31, self.a32]]
        m31 = [[self.a12, self.a13],[self.a22, self.a23]]
        m32 = [[self.a11, self.a13],[self.a21, self.a23]]
        m33 = [[self.a11, self.a12],[self.a21, self.a22]]

        detm11 = (m11[0][0] * m11[1][1]) - (m11[0][1] * m11[1][0])
        detm12 = (m12[0][0] * m12[1][1]) - (m12[0][1] * m12[1][0])
        detm13 = (m13[0][0] * m13[1][1]) - (m13[0][1] * m13[1][0])
        detm21 = (m21[0][0] * m21[1][1]) - (m21[0][1] * m21[1][0])
        detm22 = (m22[0][0] * m22[1][1]) - (m22[0][1] * m22[1][0])
        detm23 = (m23[0][0] * m23[1][1]) - (m23[0][1] * m23[1][0])
        detm31 = (m31[0][0] * m31[1][1]) - (m31[0][1] * m31[1][0])
        detm32 = (m32[0][0] * m32[1][1]) - (m32[0][1] * m32[1][0])
        detm33 = (m33[0][0] * m33[1][1]) - (m33[0][1] * m33[1][0])

        kofMatrik = [[detm11, -detm12, detm13],[-detm21, detm22, -detm23], [detm31, -detm32, detm33]]
        adjMatrik = [[kofMatrik[0][0], kofMatrik[1][0], kofMatrik[2][0]], [kofMatrik[0][1], kofMatrik[1][1], kofMatrik[2][1]], [kofMatrik[0][2], kofMatrik[1][2], kofMatrik[2][2]]]
        print(f"\nAdjoin dari matriks {self.name} = {adjMatrik}")
        return adjMatrik
    
    def invers(self) :
        determinan = self.determinan()
        if determinan == 0 :
            return print("Matriks tidak dapat dibalik dikarenakan determinan = 0")
        else :
            invers = []
            for i in self.adjoin() :
                row = []
                invers.append(row)
                for j in i :
                    elemen = self.Fraction(1/determinan * j)
                    row.append(elemen)
            print(f"\nInvers dari matriks {self.name} = {invers}")
            return invers
                
        