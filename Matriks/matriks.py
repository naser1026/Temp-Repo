from fractions import Fraction

matrik = [[3,2,-1],[1,6,3],[2,-4,0]]

a11 = matrik[0][0]
a12 = matrik[0][1]
a13 = matrik[0][2]
a21 = matrik[1][0]
a22 = matrik[1][1]
a23 = matrik[1][2]
a31 = matrik[2][0]
a32 = matrik[2][1]
a33 = matrik[2][2]

m11 = [[a22, a23],[a32, a33]]
m12 = [[a21, a23],[a31, a33]]
m13 = [[a21, a22],[a31, a32]]
m21 = [[a12, a13],[a32, a33]]
m22 = [[a11, a13],[a31, a33]]
m23 = [[a11, a12],[a31, a32]]
m31 = [[a12, a13],[a22, a23]]
m32 = [[a11, a13],[a21, a23]]
m33 = [[a11, a12],[a21, a22]]

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

detmatrik = ((a11 * a22 * a33) + (a12 * a23 * a31) + (a13 * a21 * a32)) - ((a12 * a21 * a33) + (a11 * a23 * a32) + (a13 * a22 * a31))

a = 1/detmatrik
b = []
for i in adjMatrik :
    c = []
    b.append(c)
    for j in i :
        d = Fraction(a*j)
        c.append(d)

 