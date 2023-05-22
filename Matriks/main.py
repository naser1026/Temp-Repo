from Mymatrik import Matriks
import os

os.system("cls")
matrikName = input("Masukan Nama Matriks : ")
row1 = input('Masukan Elemen Baris Pertama : ')
row2 = input('Masukan Elemen Baris Kedua : ')
row3 = input('Masukan Elemen Baris Ketiga : ')
row1 = list(map(int,row1.split(',')))
row2 = list(map(int,row2.split(',')))
row3 = list(map(int,row3.split(',')))
matrik = [row1, row2, row3]
matriks = Matriks(matrikName,matrik)
matriks.invers()