# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 20:08:23 2019

@author: Solmir741
"""

import openpyxl, xlrd
import numpy as np
wb = openpyxl.load_workbook(filename = 'test2.xlsm')
sheet = wb["Лист1"]
"""
Алгоритм основан на вычислении значения угла между стороной - вектором четырехугольника (вычисляется разность от конца к началу вектора)
и вектором от одной из вершин до введеной точки. Если вычисленное значение меньше нуля (при обходе вершин против часовой, оно будет больше нуля), то точка внутри
четырехугольника относительно рассматриваемой его стороны. Если значение больше нуля - точка снаружи. Если = 0 - точка на лежит на стороне. 
Если координаты вершины совпадаютс с координатами точки - точка в вершине.  Т.о. проводим проверку всех четырех сторон.
"""

def v_delta(x1, x2, y1, y2):
    zx = x2-x1
    zy = y2-y1
    return (zx, zy)


def v_prod (x, y):
    z=x[0]*y[1]-y[0]*x[1]
    return z

def vertex(bool_):
    for e in range(4):
        vx = float(sheet['A' + str(e + 1)].value)
        vy = float(sheet['B' + str(e + 1)].value)
        if vx == Px and vy == Py:
            return True

fl = 0

while True:
    try:
        Px = float(input("Введите координату х: "))
    except:
        print("Вы должны ввести число, попробуйте снова!")
    else:
        break

while True:
    try:
        Py = float(input("Введите координату y: "))
    except:
        print("Вы должны ввести число, попробуйте снова!")
    else:
        break

Ax0 = float(sheet['A1'].value) #координаты вершины
Ay0 = float(sheet['B1'].value)

for r in range(4):
    if r < 3:
        Ax = float(sheet['A' + str(r + 1)].value)
        Ay = float(sheet['B' + str(r + 1)].value)
        Bx = float(sheet['A' + str(r + 2)].value)
        By = float(sheet['B' + str(r + 2)].value)

    else:
        Ax = float(sheet['A' + str(r + 1)].value)
        Ay = float(sheet['B' + str(r + 1)].value)
        Bx = Ax0
        By = Ay0

    res_ = np.round(v_prod(v_delta(Ax, Bx, Ay, By), v_delta(Ax, Px, Ay, Py)), 4)
    if res_ > 0:
        print ('точка снаружи четырехугольника')
        break
    elif res_ < 0:
        fl = r
    elif res_ == 0:
        if vertex(False) == True:
            print ('точка - вершина четырехугольника')
            break
        print ('точка лежит на сторонах четырехугольника')
        break
 
if fl == 3:
    print ('точка внутри четырехугольника')



