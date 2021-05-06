#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
"""
Los atributos del criterio para la selección de proveedor son:
    Coste:                  'cost'          [0,9]
    Tiempo de entrega:      'delivery_time' [0,2]
    Garantía de calidad:    'guarantee'     [0,1]
    Calidad:                'quality'       [0,2]
La calificación de un proveedor es directamente proporcional al valor de sus atributos
(a mayor valor, mejor calificación).
Para la comparación de métodos de selección de proveedores se utilizarán los datos
contenidos en 'default_supplier_data'
"""
c_atributes = ('cost','delivery_time','guarantee','quality')
c_atributes_t = ('uint<10','uint<3','uint<2','uint<3')


def generate_suppliers(size):
    res = np.zeros((size,len(c_atributes)),np.int)
    for s in range(size):
        res[s] = [np.random.randint(10),np.random.randint(3),np.random.randint(2),np.random.randint(3)]
    return res

default_supplier_data = np.array([
    [0, 2, 0, 0],
    [4, 2, 0, 0],
    [8, 1, 0, 1],
    [9, 2, 1, 0],
    [7, 0, 1, 0],
    [6, 1, 0, 2],
    [6, 2, 1, 0],
    [1, 0, 1, 2],
    [9, 2, 0, 1],
    [5, 1, 0, 2],
    [1, 1, 1, 2],
    [5, 2, 1, 0],
    [7, 1, 1, 0],
    [9, 1, 0, 1],
    [0, 1, 0, 1],
    [6, 1, 1, 0],
    [8, 0, 0, 1],
    [6, 2, 0, 0],
    [5, 1, 1, 0],
    [2, 0, 1, 2],
    [7, 2, 0, 0],
    [5, 2, 1, 1],
    [1, 1, 0, 0],
    [4, 0, 0, 2],
    [4, 2, 1, 0],
    [1, 2, 1, 2],
    [4, 1, 1, 2],
    [5, 0, 0, 2],
    [9, 0, 1, 0],
    [2, 2, 0, 1],
    [3, 0, 1, 0],
    [7, 1, 0, 2],
    [6, 1, 1, 0],
    [1, 2, 0, 1],
    [3, 1, 0, 1],
    [4, 1, 0, 2],
    [0, 0, 1, 2],
    [2, 1, 0, 1],
    [3, 0, 1, 1],
    [8, 1, 0, 1],
    [2, 0, 1, 2],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [8, 0, 0, 0],
    [4, 0, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [9, 0, 0, 1],
    [0, 2, 0, 2],
    [8, 2, 1, 1]], dtype=np.int)
