from numpy import array, matmul, linalg

matris = array([[1, 2, 5, 6],
                [4, -4, -6, 8],
                [-12, 1, 3, 9],
                [18, 0, 0, 6]])

vektör = array([1, 6, 7, 2])

çözüm_kümesi = linalg.solve(matris, vektör)
print('Çözüm kümesi: x, y, z, t = ', çözüm_kümesi)

#alternatif çözüm
çözüm_kümesi_2 = matmul(linalg.inv(matris), vektör)
print('Çözüm kümesi_2: x, y, z, t ', çözüm_kümesi_2)